#!/usr/bin/env python3
"""Build the overview diagram and the highlighted worked-flow variants."""
import html
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DIAG = REPO / "diagrams"
IMG = REPO / "examples/img"
DETAILED = DIAG / "dataArchitectureReference.svg"

BG = "#CFDDE6"
PANEL = "#E6EDF2"
PANEL_STROKE = "#CFDDE6"
CARD = "#FFFFFF"
CARD_STROKE = "#657486"
INK = "#2D3141"
MUTED = "#4A5670"
ACCENT = "#08829C"
HILITE = "#E6F3F6"
DIM = "0.3"

MONO = "Source Code Pro, Menlo, monospace"
SANS = "DM Sans, Lato, Helvetica Neue, sans-serif"

ROWS = 6
W, M, PW, GAP = 2462, 40, 372, 30
PY, HEADER_H, CARD_PAD, CARD_TOP = 132, 52, 14, 20
CARD_H, PITCH = 54, 78
PH = HEADER_H + CARD_TOP + (ROWS - 1) * PITCH + CARD_H + 22
BAND = PY + PH + 36
H = BAND + 186

COLS = [
    ("1 · SOURCES", [
        "Internal Systems",
        "SaaS & Partners",
        "Events & Streams",
        "Files & Unstructured",
        "IoT Devices",
        "Public & Third-Party",
    ]),
    ("2 · INTEGRATION", [
        "Batch Transfer",
        "Micro-batch",
        "Streaming",
        "CDC & Replication",
        "APIs & Connectors",
        "Private Connectivity",
    ]),
    ("3 · STORAGE", [
        "Raw",
        "Standardized",
        "Curated",
        "Serving Views",
        "Materialized Views",
        "Archive & Retention",
    ]),
    ("4 · PROCESSING", [
        "Data Validation",
        "Data Transformation",
        "Data Enrichment",
        "Batch Transformation",
        "Stream Processing",
        "Schema Evolution",
    ]),
    ("5 · SERVING", [
        "SQL Access",
        "Semantic & Metric Layer",
        "Data Products",
        "REST & GraphQL APIs",
        "Federated Data Access",
        "Secure Data Sharing",
    ]),
    ("6 · CONSUMPTION", [
        "Analysts",
        "Business Users",
        "Applications & Embedded",
        "Data Scientists & ML",
        "Operational Applications",
        "Partners & External",
    ]),
]

CHIPS = [
    ("METADATA & KNOWLEDGE", "catalog · lineage · glossary", ACCENT),
    ("GOVERNANCE & TRUST", "quality · privacy · security", INK),
    ("CONTROL PLANE", "access · cost · orchestration", ACCENT),
    ("PLATFORM ENGINEERING", "CI/CD · IaC · observability", INK),
    ("ML & AI", "features · registry · drift", ACCENT),
]

CELL = {name: (i, row) for i, (_, cards) in enumerate(COLS)
        for row, name in enumerate(cards)}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def panel_x(i):
    return M + i * (PW + GAP)


def card_y(row):
    return PY + HEADER_H + CARD_TOP + row * PITCH


def text(x, y, body, family, size, fill=INK, weight=400, anchor="middle", spacing=0):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{esc(body)}</text>')


def rounded_header(x, y, w, h, r):
    return (f"M {x + r} {y} h {w - 2 * r} a {r} {r} 0 0 1 {r} {r} v {h - r} "
            f"h {-w} v {-(h - r)} a {r} {r} 0 0 1 {r} {-r} Z")


def left_block(x, y, h, r, width):
    """Rounded on the left edge only, flat on the right, like the plane rows."""
    return (f"M {x + r} {y} h {width - r} v {h} h {-(width - r)} a {r} {r} 0 0 1 "
            f"{-r} {-r} v {-(h - 2 * r)} a {r} {r} 0 0 1 {r} {-r} Z")


def build_grid(cols, *, title, subtitle, right_note, footnote, footnote_right,
               highlight=None, cells=(), chips=None):
    """Render a stage grid. Used for the overview and for the ML and AI view."""
    chips = CHIPS if chips is None else chips
    n = len(cols)
    rows = max(len(cards) for _, cards in cols)
    w = 2 * M + n * PW + (n - 1) * GAP
    ph = HEADER_H + CARD_TOP + (rows - 1) * PITCH + CARD_H + 22
    band = PY + ph + 36
    h = band + 186
    on_path = set(cells)

    out = []
    add = out.append
    add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">')
    add(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
    add('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9.2" refY="5" '
        'markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" '
        f'orient="auto"><path d="M 0.6 0.9 L 9.4 5 L 0.6 9.1 Z" fill="{MUTED}"/>'
        '</marker></defs>')

    add(text(M, 56, title, MONO, 34, weight=600, anchor="start", spacing=0.4))
    add(f'<rect x="{M}" y="76" width="{w - 2 * M}" height="3" rx="1.5" '
        f'fill="{ACCENT}"/>')
    add(text(M, 108, subtitle, MONO, 17, fill=MUTED if highlight is None else ACCENT,
             weight=600, anchor="start", spacing=1.2))
    add(text(w - M, 108, right_note, MONO, 15, fill=MUTED, weight=600,
             anchor="end", spacing=1.1))

    for i, (label, cards) in enumerate(cols):
        x = panel_x(i)
        add(f'<rect x="{x}" y="{PY}" width="{PW}" height="{ph}" rx="12" ry="12" '
            f'fill="{PANEL}" stroke="{PANEL_STROKE}" stroke-width="1.8"/>')
        add(f'<path d="{rounded_header(x, PY, PW, HEADER_H, 12)}" fill="{ACCENT}"/>')
        add(text(x + PW / 2, PY + 34, label, MONO, 23, fill="#FFFFFF",
                 weight=600, spacing=1.4))

        for row, card in enumerate(cards):
            cy = card_y(row)
            cx = x + CARD_PAD
            cw = PW - 2 * CARD_PAD
            lit = (i, row) in on_path
            faded = highlight is not None and not lit
            dimattr = ' opacity="%s"' % DIM if faded else ""
            add(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{CARD_H}" rx="6" '
                f'ry="6" fill="{HILITE if lit else CARD}" '
                f'stroke="{ACCENT if lit else CARD_STROKE}" '
                f'stroke-width="{2.4 if lit else 1.3}"{dimattr}/>')
            if lit:
                step = cells.index((i, row)) + 1
                add(f'<circle cx="{cx + 22}" cy="{cy + CARD_H / 2}" r="11" '
                    f'fill="{ACCENT}"/>')
                add(f'<text x="{cx + 22}" y="{cy + CARD_H / 2 + 4.5}" '
                    f'font-family="{MONO}" font-size="13" fill="#FFFFFF" '
                    f'font-weight="700" text-anchor="middle" '
                    f'letter-spacing="0">{step}</text>')
            add(f'<text x="{x + PW / 2}" y="{cy + 35}" font-family="{SANS}" '
                f'font-size="22" fill="{INK}" font-weight="{700 if lit else 500}" '
                f'text-anchor="middle" letter-spacing="0"'
                f'{dimattr}>{esc(card)}</text>')

    for i in range(n - 1):
        cx = panel_x(i) + PW + GAP / 2
        cy = PY + HEADER_H / 2
        add(f'<path d="M {cx - 4} {cy - 10} L {cx + 6} {cy} L {cx - 4} {cy + 10}" '
            f'fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')

    add(text(M, band, "CROSS-CUTTING PLANES  ·  APPLIES TO EVERY STAGE",
             MONO, 17, fill=MUTED, weight=600, anchor="start", spacing=1.2))

    chip_w = (w - 2 * M - (len(chips) - 1) * 24) / len(chips)
    block_w = min(236, int(chip_w * 0.44))
    label_size = 17 if block_w >= 230 else 15
    for i, (label, desc, colour) in enumerate(chips):
        x = M + i * (chip_w + 24)
        cy = band + 16
        if chip_w < 420:
            add(f'<rect x="{x}" y="{cy}" width="{chip_w}" height="96" rx="10" '
                f'ry="10" fill="{colour}"/>')
            add(text(x + chip_w / 2, cy + 54, label, MONO, 16, fill="#FFFFFF",
                     weight=600, spacing=0.5))
            continue
        add(f'<rect x="{x}" y="{cy}" width="{chip_w}" height="96" rx="10" ry="10" '
            f'fill="{PANEL if i % 2 == 0 else "#DCE7EF"}" stroke="{PANEL_STROKE}" '
            f'stroke-width="1.4"/>')
        add(f'<path d="{left_block(x, cy, 96, 10, block_w)}" fill="{colour}"/>')
        add(text(x + block_w / 2, cy + 54, label, MONO, label_size, fill="#FFFFFF",
                 weight=600, spacing=0.5))
        add(text(x + block_w + 18, cy + 54, desc, SANS, 16, fill=MUTED,
                 anchor="start"))

    add(text(M, band + 148, footnote, SANS, 17, fill=MUTED, anchor="start"))
    add(text(w - M, band + 148, footnote_right, MONO, 15, fill=MUTED,
             weight=600, anchor="end", spacing=1.1))

    wordmark = re.search(r'href="(data:image/png;base64,[^"]+)"',
                         DETAILED.read_text()).group(1)
    add(f'<image x="{w - M - 380}" y="14" width="380" height="46" '
        f'preserveAspectRatio="xMidYMid meet" href="{wordmark}"/>')

    add("</svg>")
    return "\n".join(out) + "\n"


def build_overview(highlight=None, title=None):
    """highlight: list of card names, in flow order; None renders the neutral view."""
    cells = [CELL[n] for n in (highlight or [])]
    if highlight is None:
        subtitle = "SIX STAGES. ONE RESPONSIBILITY EACH. EVERY BOX IS OPTIONAL."
        right_note = "WORKED FLOWS IN examples/"
    else:
        subtitle = "WORKED FLOW  ·  " + title
        right_note = "TEAL CARDS PARTICIPATE  ·  FADED CARDS DO NOT"
    return build_grid(
        COLS, title="ENTERPRISE DATA PLATFORM  ·  ARCHITECTURE OVERVIEW",
        subtitle=subtitle, right_note=right_note, highlight=highlight, cells=cells,
        footnote="Not every dataset crosses every stage; each flow uses a subset "
                 "of these boxes.",
        footnote_right="CAPABILITY-LEVEL DETAIL IN THE REFERENCE DIAGRAM")


ML_COLS = [
    ("1 · INPUTS", [
        "Governed Datasets",
        "Unstructured Content",
        "Feedback & Labels",
        "Reference Data",
    ]),
    ("2 · FEATURES", [
        "Feature Engineering",
        "Feature Store",
        "Point-in-Time Joins",
        "Feature Versions",
    ]),
    ("3 · TRAINING", [
        "Experiment Tracking",
        "Training Runs",
        "Evaluation & Benchmarks",
        "Hyperparameter Search",
    ]),
    ("4 · DEPLOY", [
        "Model Registry",
        "Approval & Promotion",
        "Model Serving",
        "Batch Scoring",
    ]),
    ("5 · MONITOR", [
        "Drift Detection",
        "Quality Gates",
        "Model Observability",
        "Retraining Loop",
    ]),
]


def build_ml_view():
    return build_grid(
        ML_COLS, title="ENTERPRISE DATA PLATFORM  ·  ML AND AI",
        subtitle="FIVE STAGES OF THE MODEL TOOL CHAIN. EVERY BOX IS OPTIONAL.",
        right_note="WORKED FLOW IN examples/",
        footnote="These capabilities live in the ML and AI band of the "
                 "capability inventory.",
        footnote_right="INPUTS COME FROM THE GOVERNED ZONES")


# ---------------------------------------------------------------- detailed view

RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" '
                     r'height="([\d.]+)" rx="6"')
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')


def parse_cards(svg):
    lines = svg.splitlines()
    cards = []
    for idx, ln in enumerate(lines):
        m = RECT_RE.match(ln.strip())
        if not m:
            continue
        x, y, w, h = map(float, m.groups())
        if h >= 40:
            cards.append({"line": idx, "x": x, "y": y, "w": w, "h": h,
                          "texts": []})
    by_line = {c["line"]: c for c in cards}
    for idx, ln in enumerate(lines):
        m = TEXT_RE.match(ln.strip())
        if not m:
            continue
        tx, ty = float(m.group(1)), float(m.group(2))
        for c in cards:
            if c["x"] - 1 <= tx <= c["x"] + c["w"] + 1 and c["y"] < ty <= c["y"] + c["h"]:
                c["texts"].append(idx)
                break
    return lines, cards, by_line


def _is_landmark(stripped):
    """Column header bars, column titles and cross-cutting plane labels stay legible."""
    if stripped.startswith("<path") and "a 12 12" in stripped:
        return True
    if 'font-size="30"' in stripped or 'font-size="28"' in stripped:
        return True
    if stripped.startswith('<rect x="40"') and 'width="460"' in stripped:
        return True
    return False


def _is_soft(stripped):
    """Band backgrounds and in-column section labels keep some structure."""
    if stripped.startswith('<rect x="40"') and 'width="3320"' in stripped:
        return True
    if "Source Code Pro" in stripped and 'font-size="16.5"' in stripped:
        return True
    return False


def render_detailed(selected):
    svg = DETAILED.read_text()
    lines, cards, _ = parse_cards(svg)
    lookup = {}
    seen = {}
    for c in cards:
        label = " ".join(html.unescape(re.sub(r"<[^>]+>", "",
                                              lines[i].split(">", 1)[1].rsplit("<", 1)[0]))
                         for i in c["texts"])
        key = " ".join(label.split())
        seen.setdefault(key, []).append(c)
        lookup[f"{key}#{len(seen[key]) - 1}"] = c
        lookup.setdefault(key, c)

    missing = [s for s in selected if s not in lookup]
    if missing:
        raise SystemExit(f"unmatched labels: {missing}")

    lit_rects = {lookup[s]["line"] for s in selected}
    lit_texts = {i for s in selected for i in lookup[s]["texts"]}
    out = []
    for idx, ln in enumerate(lines):
        stripped = ln.strip()
        if idx == 0 or stripped.startswith('<rect width="3400"'):
            out.append(ln)
            continue
        if idx == 2 or idx == 3:
            out.append(ln)
            continue
        if stripped.startswith("<image"):
            out.append(ln)
            continue
        if idx in lit_rects:
            c = next(c for c in cards if c["line"] == idx)
            out.append(f'<rect x="{c["x"]}" y="{c["y"]}" width="{c["w"]}" '
                       f'height="{c["h"]}" rx="6" ry="6" fill="{HILITE}" '
                       f'stroke="{ACCENT}" stroke-width="3.2"/>')
            continue
        if idx in lit_texts:
            head, rest = ln.split(">", 1)
            head = re.sub(r'fill="[^"]*"', f'fill="{INK}"', head)
            head = re.sub(r'font-weight="[^"]*"', 'font-weight="700"', head)
            out.append(head + ">" + rest)
            continue
        if stripped.startswith("<rect") and RECT_RE.match(stripped) and \
                float(RECT_RE.match(stripped).group(4)) >= 40:
            out.append(ln.replace("/>", f' opacity="{DIM}"/>', 1))
            continue
        if _is_landmark(stripped):
            out.append(ln)
            continue
        if _is_soft(stripped):
            attr = ' opacity="0.62"'
            out.append(ln.replace(">", f"{attr}>", 1) if stripped.startswith("<text")
                       else ln.replace("/>", f"{attr}/>", 1))
            continue
        if stripped.startswith("<text") or stripped.startswith("<rect") or \
                stripped.startswith("<path"):
            out.append(ln.replace(">", f' opacity="{DIM}">', 1) if stripped.startswith("<text")
                       else ln.replace("/>", f' opacity="{DIM}"/>', 1))
            continue
        out.append(ln)
    return "\n".join(out) + "\n"



EXAMPLES = {
    "finance-reporting": {
        "title": "FINANCE REPORTING, ERP AND CRM",
        "tagline": "batch, ERP and CRM, published as a governed data product",
        "overview": ["Internal Systems", "Batch Transfer", "Raw", "Standardized",
                     "Curated", "Batch Transformation", "Data Products",
                     "Business Users"],
        "detailed": [
            "Databases", "Applications", "Batch",
            "Database Connectivity (JDBC/ODBC)", "Private Service Connectivity",
            "Raw", "Standardized", "Curated",
            "Batch Processing", "Data Transformation", "Data Validation",
            "Data Marts", "SQL Access", "Semantic Models", "Metric Models",
            "Business Metrics & KPIs", "Data Products",
            "Analysts", "Business Users", "Analytics & Reporting",
            "Enterprise Catalog", "Data Lineage", "Data Quality",
            "Contract Policies", "Access Management", "Workflow & Orchestration",
            "CI/CD & DevOps", "Observability & Monitoring",
        ],
    },
    "customer-360": {
        "title": "CUSTOMER 360, STREAMING",
        "tagline": "streaming, one identity per customer, served inside an app",
        "overview": ["SaaS & Partners", "Streaming", "Raw", "Standardized",
                     "Curated", "Stream Processing", "Data Products",
                     "Applications & Embedded"],
        "detailed": [
            "SaaS Applications", "Applications", "Messages & Events",
            "Streaming", "CDC (Change Data Capture)", "Event Streaming",
            "Raw", "Standardized", "Curated",
            "Stream Processing", "Data Enrichment", "Data Validation",
            "Published Datasets", "Data Products", "REST APIs", "Semantic Models",
            "Business Definitions", "Data Scientists", "Application Teams",
            "Operational Applications", "Embedded Analytics (in-app)",
            "Enterprise Catalog", "Data Lineage", "Data Quality",
            "Data Contracts Enforcement", "Access Management",
            "Workflow & Orchestration", "Observability & Monitoring",
        ],
    },
    "ml-and-ai": {
        "title": "ML AND AI FEATURES",
        "tagline": "batch features for models, stopping where the reference stops",
        "overview": ["Internal Systems", "Files & Unstructured", "Batch Transfer",
                     "Raw", "Standardized", "Curated", "Data Enrichment",
                     "SQL Access", "Data Scientists & ML"],
        "detailed": [
            "Databases", "Files & Documents", "Unstructured Data", "Batch",
            "File Transfer (FTP/SFTP)", "Raw", "Standardized", "Curated",
            "Batch Processing", "Data Transformation", "Data Enrichment",
            "Data Validation", "Published Datasets", "SQL Access",
            "Feature Store", "Experiment Tracking", "Model Registry",
            "Model Serving", "Evaluation & Drift",
            "Data Scientists", "ML Engineers", "Advanced Analytics & Data Science",
            "Enterprise Catalog", "Data Lineage", "Data Quality",
            "Workflow & Orchestration", "Observability & Monitoring",
        ],
    },

    "federated-reporting": {
        "title": "FEDERATED REPORTING, NO COPY",
        "tagline": "query in place, nothing landed",
        "overview": ["Public & Third-Party", "APIs & Connectors", "Data Validation",
                     "Federated Data Access", "Analysts"],
        "detailed": [
            "Third-Party Data", "External Databases", "External Files", "APIs#0",
            "Database Connectivity (JDBC/ODBC)", "Data Validation",
            "Data Virtualization", "Federated Data Access", "Analysts",
            "Business Users", "Enterprise Catalog", "Data Lineage", "Data Quality",
            "Access Management",
        ],
    },
    "realtime-alerts": {
        "title": "REAL-TIME ALERTS",
        "tagline": "events processed in flight, pushed back as REST calls",
        "overview": ["Events & Streams", "Streaming", "Curated", "Stream Processing",
                     "REST & GraphQL APIs", "Applications & Embedded"],
        "detailed": [
            "Messages & Events", "Streaming Data", "Streaming", "Event Streaming",
            "Publish & Subscribe", "Curated", "Stream Processing", "Event Processing",
            "Data Enrichment", "REST APIs", "GraphQL APIs", "Application Teams",
            "Operational Applications", "Embedded Analytics (in-app)",
            "Data Contracts Enforcement", "Observability & Monitoring",
            "Workflow & Orchestration",
        ],
    },
    "secure-data-sharing": {
        "title": "SECURE DATA SHARING",
        "tagline": "replicated, contracted, shared outward with a partner",
        "overview": ["Internal Systems", "CDC & Replication", "Private Connectivity",
                     "Raw", "Standardized", "Data Validation", "Secure Data Sharing",
                     "Partners & External"],
        "detailed": [
            "Databases", "Applications", "CDC (Change Data Capture)",
            "Log-Based Replication", "Dedicated Private Connectivity", "Raw",
            "Standardized",
            "Data Validation",
            "Data Enrichment", "Secure Data Sharing", "Data Exchange",
            "Business Definitions", "Partner Applications", "Partners",
            "Contract Policies", "Data Product Governance", "Policy as Code",
            "Access Management", "Lifecycle, Retention & Deletion",
            "Audit & Compliance Reporting",
        ],
    },
    "compliance-retention": {
        "title": "RETENTION AND AUDIT",
        "tagline": "kept for years, provable, then deleted",
        "overview": ["Internal Systems", "Batch Transfer", "Raw", "Archive & Retention",
                     "Data Validation", "SQL Access", "Partners & External"],
        "detailed": [
            "Databases", "Applications", "Batch",
            "Database Connectivity (JDBC/ODBC)", "Raw", "Data Validation",
            "Published Datasets", "SQL Access", "Partners", "External Consumers",
            "Enterprise Catalog", "Data Lineage", "Data Classification", "Data Quality",
            "Contract Policies", "Lifecycle, Retention & Deletion", "Policy as Code",
            "Audit & Compliance Reporting", "Access Management",
            "Workflow & Orchestration",
        ],
    },
    "self-service-bi": {
        "title": "SELF-SERVICE BI",
        "tagline": "curated facts, serving views, one semantic layer",
        "overview": ["Internal Systems", "CDC & Replication", "Raw", "Standardized",
                     "Curated", "Serving Views", "Materialized Views",
                     "Data Transformation", "Semantic & Metric Layer", "Analysts",
                     "Business Users"],
        "detailed": [
            "Databases", "Applications", "CDC (Change Data Capture)",
            "Log-Based Replication", "Raw", "Standardized", "Curated",
            "Serving Views",
            "Data Transformation", "Materialized Views", "Semantic Models",
            "Metric Models", "Business Metrics & KPIs", "Semantic Query APIs",
            "Analysts", "Business Users", "Self-Service Analytics",
            "Enterprise Catalog", "Data Lineage", "Data Quality",
            "Access Management", "Workflow & Orchestration",
            "Observability & Monitoring",
        ],
    },
    "iot-telemetry": {
        "title": "IOT TELEMETRY",
        "tagline": "millions of small records, acted on in seconds",
        "overview": ["IoT Devices", "Micro-batch", "Raw", "Curated",
                     "Stream Processing", "Schema Evolution", "REST & GraphQL APIs",
                     "Operational Applications"],
        "detailed": [
            "IoT Devices#0", "Messages & Events", "Micro-batch", "Raw", "Curated",
            "Stream Processing", "Schema Evolution", "Data Validation", "REST APIs",
            "Operational Applications", "Downstream Systems",
            "Data Contracts Enforcement", "Observability & Monitoring",
            "Workflow & Orchestration",
        ],
    },
}

def build_all():
    """Return every generated SVG as {relative path: text}."""
    out = {"diagrams/dataArchitectureOverview.svg": build_overview(),
           "diagrams/mlAiOverview.svg": build_ml_view()}
    for slug, spec in EXAMPLES.items():
        out[f"examples/img/{slug}-overview.svg"] = build_overview(
            spec["overview"], spec["title"])
        out[f"examples/img/{slug}-inventory.svg"] = render_detailed(
            spec["detailed"])
    return out


if __name__ == "__main__":
    for rel in build_all():
        print(rel)
