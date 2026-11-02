#!/usr/bin/env python3
"""Build or verify the generated artefacts in this repository.

    python3 -m tools.build --check    # fail if anything on disk is stale (CI)
    python3 -m tools.build --write    # regenerate the SVGs, PNGs and pages
    python3 -m tools.build --render   # re-render PNGs from the committed SVGs

The SVGs in diagrams/ and examples/img/, the example pages, and the
"Worked Flows That Use This Stage" block in each guide chapter are all
generated. Hand-edit tools/diagram_builder.py or tools/page_builder.py instead.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from tools import diagram_builder, page_builder

REPO = diagram_builder.REPO
PNG_ZOOM = {"inventory": "0.8"}


def generated():
    out = {}
    out.update(diagram_builder.build_all())
    out.update(page_builder.build_all())
    return out


def stale(out):
    bad = []
    for rel, text in out.items():
        path = REPO / rel
        if not path.exists() or path.read_text() != text:
            bad.append(rel)
    return sorted(bad)


def write(out):
    for rel, text in out.items():
        path = REPO / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    print(f"wrote {len(out)} files")


def render(paths):
    resvg = shutil.which("resvg")
    if not resvg:
        sys.exit("resvg not found; install it or render the SVGs elsewhere")
    pngquant = shutil.which("pngquant")
    for svg in paths:
        svg = Path(svg)
        png = svg.with_suffix(".png")
        cmd = [resvg]
        if "inventory" in svg.name:
            cmd += ["-z", PNG_ZOOM["inventory"]]
        subprocess.run(cmd + [str(svg), str(png)], check=True)
        if pngquant:
            subprocess.run([pngquant, "--force", "--quality", "80-95",
                            "--output", str(png) + ".tmp", str(png)], check=True)
            Path(str(png) + ".tmp").replace(png)
        print(f"rendered {png.relative_to(REPO)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero when generated files are stale")
    ap.add_argument("--write", action="store_true", help="regenerate everything")
    ap.add_argument("--render", action="store_true",
                    help="re-render PNGs from the SVGs")
    args = ap.parse_args()

    out = generated()

    if args.check:
        bad = stale(out)
        if bad:
            print("stale generated files:")
            for rel in bad:
                print(f"  {rel}")
            print("\nrun: python3 -m tools.build --write")
            sys.exit(1)
        print(f"up to date ({len(out)} generated files)")
        return

    if args.write:
        write(out)
        render([REPO / rel for rel in out if rel.endswith(".svg")])
        return

    if args.render:
        render(sorted(REPO.glob("diagrams/*.svg")) +
               sorted(REPO.glob("examples/img/*.svg")))
        return

    ap.print_help()


if __name__ == "__main__":
    main()