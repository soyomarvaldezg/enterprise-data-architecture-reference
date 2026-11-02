# Contributing

This is a living document. Corrections, sharper wording, and missing
capabilities are all welcome.

## What belongs here

- **Capabilities, not products.** The reference is deliberately vendor-neutral. A change
  that names a specific tool belongs in an implementation guide, not in this architecture.
- **One concern per box.** If a proposed box is really two responsibilities, argue for the
  split. If a new box only restates a neighbour, argue for the removal instead.
- **Plain language.** The audience includes people who do not work in data engineering.
  If a sentence only lands for someone who already knows the answer, rewrite it.

## Proposing a change

1. Open an issue describing what should change and why. If it affects the diagrams, say
   which stage or plane.
2. For anything larger than a wording fix, wait for agreement before writing the code. A
   capability added to one diagram usually has to appear in the guide, the inventory, and
   at least one worked flow.
3. Submit a pull request. Keep the technology-agnostic, educational tone.

## Regenerating the diagrams and pages

The following are generated, not hand-written:

| Generated | From |
| --- | --- |
| `diagrams/dataArchitectureOverview.svg`, `diagrams/mlAiOverview.svg` and their PNGs | `tools/diagram_builder.py` |
| `examples/img/*.svg` and their PNGs | `tools/diagram_builder.py` |
| `examples/*.md` | `tools/page_builder.py` |
| the "Worked Flows That Use This Stage" block in each guide chapter | `tools/page_builder.py` |

```bash
python3 -m tools.build --check   # fail if anything on disk is stale
python3 -m tools.build --write   # regenerate SVGs, PNGs and pages
```

`--check` is the useful one in review: it fails when a diagram or page no longer matches
its source. Rendering needs [resvg](https://github.com/linebender/resvg); `pngquant` is
used when available to keep the PNGs small.

The two hand-authored files, `diagrams/dataArchitectureReference.svg` and the guide
chapters, are edited directly. The inventory diagram is laid out with absolute
coordinates, so text changes that alter a card's width may need the box widened by hand.

## Before opening a pull request

- `python3 -m tools.build --check` passes.
- Every new capability appears in the inventory, and in the guide chapter that owns it.
- If you add a worked flow, add it to `ORDER` in `tools/page_builder.py` so the index,
  the matrix, and the guide cross-links pick it up.