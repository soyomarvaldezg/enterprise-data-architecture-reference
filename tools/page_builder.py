#!/usr/bin/env python3
"""Generate the examples/ markdown pages from the same data the images use."""
import re
from pathlib import Path

from tools import diagram_builder as bd

REPO = bd.REPO
EX = REPO / "examples"

svg = bd.DETAILED.read_text()
lines, cards, _ = bd.parse_cards(svg)

coords, groups = {}, {}
for c in cards:
    label = " ".join(
        bd.html.unescape(re.sub(r"<[^>]+>", "",
                                lines[i].split(">", 1)[1].rsplit("<", 1)[0]))
        for i in c["texts"])
    key = " ".join(label.split())
    groups.setdefault(key, []).append((c["x"], c["y"]))
    coords[key] = (c["x"], c["y"])
    coords[f"{key}#{len(groups[key]) - 1}"] = (c["x"], c["y"])


def plane(x, y):
    """Which cross-cutting plane or column a card belongs to, from its position."""
    if y >= 1400:
        return {1502: "Metadata & Knowledge", 1660: "Governance & Trust",
                1818: "Control Plane", 1976: "Platform Engineering",
                2134: "ML & AI"}[int(y)]
    if x < 500:
        return "Data Sources"
    if x < 1200:
        return "Integration Plane"
    if x < 1900:
        return "Enterprise Platform"
    if x < 2700:
        return "Serving & Data Products"
    return "Data Consumption"


GUIDE = {
    "Data Sources": "../guide/01-data-sources.md",
    "Integration Plane": "../guide/02-integration-plane.md",
    "Enterprise Platform": "../guide/03-enterprise-platform.md",
    "Serving & Data Products": "../guide/04-serving-access.md",
    "Data Consumption": "../guide/06-consumption.md",
    "Metadata & Knowledge": "../guide/07-metadata-knowledge.md",
    "Governance & Trust": "../guide/08-governance-trust.md",
    "Control Plane": "../guide/09-control-plane.md",
    "Platform Engineering": "../guide/10-platform-engineering.md",
    "ML & AI": "../README.md#ml-and-ai-a-second-tool-chain",
}

STAGE_GUIDE = {
    "Sources": "../guide/01-data-sources.md",
    "Integration": "../guide/02-integration-plane.md",
    "Storage": "../guide/03-enterprise-platform.md",
    "Processing": "../guide/03-enterprise-platform.md",
    "Serving": "../guide/04-serving-access.md",
    "Consumption": "../guide/06-consumption.md",
}

PLAIN = {
    "Access Management": "Who is allowed to read what.",
    "Advanced Analytics & Data Science": "Statistical work that goes past reporting.",
    "Analysts": "People who answer business questions with data.",
    "Analytics & Reporting": "Dashboards and regular reports.",
    "APIs": "An agreed interface for pulling data out.",
    "Application Teams": "Engineers building software on the platform.",
    "Applications": "The software the business runs on: ERP, CRM, billing.",
    "Audit & Compliance Reporting": "Evidence, on demand, that the rules were followed.",
    "Batch": "Move a whole day of data at once, on a schedule.",
    "Batch Processing": "Reshape data in bulk, on a schedule.",
    "Business Definitions": "What a business term means, written down once.",
    "Business Metrics & KPIs": "The numbers the business actually reports.",
    "Business Users": "People who read dashboards and never write SQL.",
    "CDC (Change Data Capture)": "Read the database's change log instead of dumping tables.",
    "CI/CD & DevOps": "Ship platform changes safely, the same way every time.",
    "Contract Policies": "Agreed rules about what a dataset will contain.",
    "Curated": "Joined, deduplicated, modelled, and trusted enough to publish.",
    "Data Contracts Enforcement": "Fail loudly, at the producer, when the promise is broken.",
    "Data Enrichment": "Add context from other data before anyone uses it.",
    "Data Exchange": "A governed hand-off of data to another organisation.",
    "Data Lineage": "A map of where data came from and what it feeds.",
    "Data Marts": "A small store built for one team's questions.",
    "Data Product Governance": "Who owns a product, and what it promises.",
    "Data Quality": "Checks that data is correct, complete and on time.",
    "Data Scientists": "People who build models and run experiments.",
    "Data Transformation": "Reshape data: clean it, join it, aggregate it.",
    "Data Validation": "Check data meets its rules before anyone relies on it.",
    "Data Virtualization": "A query layer that hides where the data physically sits.",
    "Database Connectivity (JDBC/ODBC)": "The standard way to open a database connection.",
    "Databases": "Where applications keep their records of truth.",
    "Embedded Analytics (in-app)": "Charts shown inside another product's screens.",
    "Enterprise Catalog": "The index of what data exists, and where.",
    "Event Processing": "React to a single event while it is in flight.",
    "Event Streaming": "A durable log of events that many readers can consume.",
    "External Databases": "A database another organisation owns.",
    "External Files": "Files a partner drops on a schedule.",
    "Federated Data Access": "Query across sources without landing a copy.",
    "File Transfer (FTP/SFTP)": "Move files over a secure file protocol.",
    "Files & Documents": "Spreadsheets, PDFs, exports and shared drives.",
    "Data Products": "A packaged, documented, supported dataset with a promise attached.",
    "GraphQL APIs": "A query interface where the client asks for exactly the fields it wants.",
    "Lifecycle, Retention & Deletion": "How long data is kept, and how it is really removed.",
    "Messages & Events": "Signals applications send each other as things happen.",
    "Metric Models": "One agreed definition per number, computed in one place.",
    "ML Engineers": "People who put models into production and keep them there.",
    "Observability & Monitoring": "Noticing when something is broken, slow or late.",
    "Operational Applications": "The systems running the business, now fed by the platform.",
    "Partner Applications": "Software a partner runs against your data.",
    "Partners": "Other organisations you exchange data with, under contract.",
    "Policy as Code": "Rules written as code, so they can be tested and versioned.",
    "Private Service Connectivity": "A private network path instead of the public internet.",
    "Publish & Subscribe": "One publisher, many subscribers, decoupled in time.",
    "Published Datasets": "A dataset released, deliberately, for others to consume.",
    "Raw": "The data exactly as it arrived, untouched.",
    "Log-Based Replication": "Keep a running copy of another system by reading its log.",
    "REST APIs": "A simple request-and-response interface for applications.",
    "SaaS Applications": "Cloud tools: a hosted CRM, billing or support system.",
    "Secure Data Sharing": "Grant access inside your own boundary, without exporting a file.",
    "Semantic Models": "Business-friendly definitions sitting over physical tables.",
    "SQL Access": "Ask questions in SQL over a governed connection.",
    "Standardized": "Same names, types and codes regardless of which system it came from.",
    "Stream Processing": "Reshape data as it flows, before it lands.",
    "Streaming": "Move records continuously, as they arrive.",
    "Streaming Data": "A continuous feed rather than a nightly dump.",
    "Third-Party Data": "Data you buy or subscribe to from a vendor.",
    "Unstructured Data": "Text, images, audio: data with no fixed columns.",
    "Workflow & Orchestration": "Deciding what runs when, in what order, and what to do on failure.",
    "Data Classification": "Labelling data by how sensitive it is.",
    "External Consumers": "People outside the company who are allowed to see the data.",
    "Encryption & Key Management": "Data scrambled at rest and in transit, and who holds the keys.",
    "Identity & Authentication": "Proving who a person or a service is, once.",
    "Data Masking & Tokenization": "Showing a redacted value instead of the real one.",
    "Data Privacy": "Limiting what personal data is collected, used and kept.",
    "IoT Devices": "Sensors and machines reporting their own state.",
    "Dedicated Private Connectivity": "A private circuit to a partner, not the public internet.",
    "Micro-batch": "Small batches every few seconds, a step short of full streaming.",
    "Schema Evolution": "Handling a source that changes shape without breaking what is downstream.",
    "Serving Views": "Views and stored query results built for consumers, not new source records.",
    "Materialized Views": "Query results stored and refreshed so dashboards do not recompute them.",
    "Downstream Systems": "Other systems that consume the data and act on it.",
    "Self-Service Analytics": "Business users answering their own questions without raising a ticket.",
    "Semantic Query APIs": "Ask for data using business terms instead of table names.",
    "Feature Store": "Model inputs computed once and served the same way to training and to production.",
    "Experiment Tracking": "A record of what was tried, with which data and which settings.",
    "Model Registry": "The list of which models exist, what they were trained on, and which is live.",
    "Model Serving": "Answering predictions through an endpoint instead of a query.",
    "Vector Index": "A lookup that finds similar text, images or records by meaning.",
    "Evaluation & Drift": "Checking whether a model is still right months after launch.",
}

WHY = {
    "finance-reporting": [
        "It is the flow almost every organisation already runs, so it is the honest baseline: if this one is hard, nothing else will be easy.",
        "It forces the reconciliation question. ERP and CRM disagree about the same customer, so `Standardized` has to mean something concrete.",
        "It ends in a number that leaves the building. That is why contract policies, quality checks and lineage sit on the path rather than beside it.",
    ],
    "customer-360": [
        "It is the flow that tells you whether ingestion, storage and processing are genuinely separate concerns. The same three zones serve batch and streaming unchanged.",
        "It forces identity resolution: one person, three systems, two spellings of their name.",
        "The consumer is an application, so latency and contract stability outrank completeness. A wrong number delivered in 40 seconds is still wrong.",
    ],
    "ml-and-ai": [
        "It proves the platform is not only for reporting. Features come from the same governed zones as BI, which is the cheap part nobody disputes.",
        "It forces versioning. A model has to know which version of which dataset it learned from, or a regression is untraceable.",
        "It is the flow that shows the second tool chain is not a separate universe: the features come from the same governed zones as BI.",
    ],
    "federated-reporting": [
        "It is the counter-example to every land-everything platform. Some data should never be copied: small, regulated, or changing faster than your pipeline runs.",
        "It is the cheapest test of whether storage and access are truly decoupled. If a query needs a landing zone, they are not.",
        "It exposes the cost of no copy: with nothing stored, the catalog and lineage are the only evidence you have when a number looks wrong.",
    ],
    "realtime-alerts": [
        "It compresses the pipeline into seconds and shows what falls away under that constraint: raw landing, batch transformation, reports, analysts.",
        "It forces the contract question, because an alert consumer breaks the moment a schema changes silently at 2am.",
        "It proves serving is not only SQL and dashboards. A REST call into an operational app is a first-class publish mode.",
    ],
    "secure-data-sharing": [
        "It is where governance stops being paperwork. The data leaves your boundary and you still own the obligations attached to it.",
        "It forces the difference between an internal mart and a contracted external shape. Your reporting model is not what a partner signed up for.",
        "It exercises the least-used parts of the inventory: retention, deletion, audit reporting and policy as code.",
    ],
    "self-service-bi": [
        "It is the flow everyone means when they say \"the data platform\", and the one most often built badly: every dashboard rebuilding the same logic in its own SQL.",
        "It settles the difference between gold and serving. Curated holds facts and dimensions; serving holds the views and precomputed results that BI actually reads.",
        "Materialized views are on the path because a dashboard that recomputes a year of facts on every refresh is a cost problem before it is a latency problem.",
    ],
    "iot-telemetry": [
        "It makes \"high volume, small records\" concrete: one factory floor can outproduce every business application in the company combined.",
        "It shows why micro-batch exists at all. A full stream stack is hard to operate, and thirty-second batches keep the line running just as well.",
        "It is the flow where schema evolution stops being theoretical: devices get new firmware and start sending fields nobody designed for.",
    ],
    "compliance-retention": [
        "It turns a policy sentence into a pipeline: keep records readable for years, then prove they are gone.",
        "It is the only flow where deletion is a feature rather than an accident. Auditors ask for evidence, not assurances.",
        "It exercises the least-used box in the overview, `Archive & Retention`, which until now was an untested claim.",
    ],
}

PROSE = {
    "finance-reporting": dict(
        title="Finance reporting from an ERP and CRM",
        lead=("A batch flow. Two operational systems land once a night, conform through "
              "the three storage zones, and publish a governed financial data product. "
              "It is the smallest flow that still exercises the whole platform, which is "
              "why it is the first example."),
        unused=["Streaming", "CDC & Replication", "Event Processing", "GraphQL APIs",
                "IoT Devices", "Public Data", "External Consumers"],
        notes=[
            "Batch transfer and JDBC connectivity are enough; no streaming path is needed.",
            "Standardized is where ERP and CRM customer and cost centres are conformed, so "
            "the financial numbers reconcile across systems.",
            "Contract Policies and Data Quality sit on the path because the numbers are "
            "published outside the platform, where they cannot be corrected silently.",
        ],
    ),
    "customer-360": dict(
        title="Customer 360 from operational systems",
        lead=("A streaming flow. SaaS activity and operational events are captured "
              "continuously, standardized into one customer identity, and served as an "
              "embedded product inside operational applications. Correctness within "
              "minutes matters more than completeness within a day."),
        unused=["Batch Transfer", "Micro-batch", "File Transfer", "SQL Access",
                "Business Users", "External Consumers"],
        notes=[
            "Streaming and CDC replace batch transfer; the storage zones stay the same, "
            "which is the point of keeping ingestion separate from storage.",
            "Stream Processing does identity resolution and enrichment before the record "
            "reaches the curated zone, because the consumer is an application, not a report.",
            "Data Contracts Enforcement is on the path: an embedded product breaks the "
            "moment the contract changes without warning.",
        ],
    ),
    "ml-and-ai": dict(
        title="ML and AI features from governed data",
        lead=("Features for models are built from the same governed zones as BI. That part "
              "is cheap and it is where most platforms already succeed. The flow stops "
              "where this reference architecture stops."),
        diagram=("[ML and AI view](../diagrams/mlAiOverview.png) — the tool chain that "
                 "the capabilities below belong to."),
        unused=["Streaming", "CDC & Replication", "Stream Processing", "GraphQL APIs",
                "Semantic Models", "Business Users", "Data Products"],
        notes=[
            "Unstructured Data and Files & Documents are on the path; a model does not only "
            "read tables.",
            "Schema Evolution and Data Validation matter more here than in BI: a silent "
            "column change becomes a silently wrong model.",
            "Data Lineage is not optional. Without it, a regression cannot be traced to the "
            "dataset version that caused it.",
            "No data product is published here. The consumer is a scientist or a training "
            "job reading governed datasets through SQL Access, which is a different publish "
            "mode, not a lesser one.",
        ],
        followup=("The flow leaves the six data stages at SQL Access and continues in the "
                  "ML and AI band of the inventory. That band is drawn in full, with the "
                  "connections between the boxes, in the "
                  "[ML and AI view](../diagrams/mlAiOverview.png)."),
    ),
    "federated-reporting": dict(
        title="Federated reporting without copying data",
        lead=("A query-time flow. Third-party data is read where it already lives, "
              "validated against its contract at read time, and federated into the "
              "analyst's tool. Nothing is landed, so the Storage stage is empty on "
              "purpose."),
        unused=["Batch Transfer", "CDC & Replication", "Raw", "Standardized", "Curated",
                "Data Products", "Semantic & Metric Layer"],
        notes=[
            "Storage is empty. If nothing is landed, raw, standardized and curated do not "
            "exist for this flow, and pretending otherwise is how reference architectures "
            "become shelfware.",
            "Validation moves to the read path: the check runs when the query runs, so a "
            "broken source fails loudly at the desk instead of silently overnight.",
            "Enterprise Catalog and Data Lineage carry more weight here, because there is "
            "no stored copy left to inspect when something looks wrong.",
        ],
    ),
    "realtime-alerts": dict(
        title="Real-time alerts from event streams",
        lead=("A sub-minute flow. Operational events are consumed continuously, processed "
              "in flight, and pushed back into the application that has to act on them. "
              "There is no report and no analyst in the loop."),
        unused=["Batch Transfer", "Raw", "SQL Access", "Data Products",
                "Business Users", "Semantic & Metric Layer"],
        notes=[
            "The stream lands in Curated directly. Raw landing would add minutes of latency "
            "for no correctness gain on this flow.",
            "Event Processing, not Batch Transformation: the consumer is an application "
            "waiting on a decision, not a job running at midnight.",
            "Data Contracts Enforcement is on the path. An alert consumer breaks the moment "
            "the event schema changes without warning.",
        ],
    ),
    "compliance-retention": dict(
        title="Retention and audit",
        lead=("A slow, boring, legally required flow. Records land once, are held for "
              "years under a retention rule, can be queried by an auditor on demand, "
              "and must eventually be deleted with proof. Nothing here is fast, and "
              "that is the point."),
        unused=["Streaming", "CDC & Replication", "Standardized", "Curated",
                "Serving", "Materialized Views", "Data Products",
                "Semantic & Metric Layer", "Business Users"],
        notes=[
            "Only Raw is used before the archive. Standardizing seven-year-old data for "
            "a one-off audit is wasted effort, and the auditor wants the record as it "
            "was received.",
            "SQL Access is on the path because the auditor runs their own queries. A "
            "report someone else ran is not evidence.",
            "Lifecycle, Retention & Deletion and Audit & Compliance Reporting are the "
            "point of the flow, not supporting cast.",
        ],
    ),
    "self-service-bi": dict(
        title="Self-service BI on a semantic layer",
        lead=("The classic self-service flow. Analysts query a governed model rather than "
              "raw tables, dashboards read precomputed results rather than recomputing "
              "facts, and the numbers agree because the definitions live in one place."),
        unused=["Streaming", "Micro-batch", "Data Products", "REST & GraphQL APIs",
                "Federated Data Access", "Secure Data Sharing"],
        notes=[
            "Serving Views and Materialized Views are two steps on purpose. A logical view "
            "is a saved query evaluated on every read; a materialized view stores the "
            "results and refreshes them in the background.",
            "Data Transformation sits here rather than Batch Transformation, because the "
            "work is modelling facts and dimensions, not moving files around.",
            "The semantic layer is what stops every team computing revenue their own way. "
            "It is also where self-service usually fails, when the definitions are wrong "
            "or nobody owns them.",
        ],
    ),
    "iot-telemetry": dict(
        title="IoT telemetry from the factory floor",
        lead=("A machine-generated flow. Sensors emit small records continuously, a "
              "gateway micro-batches them, and the platform turns them into signals that "
              "operations acts on. Nobody writes a report and nobody queries a table."),
        unused=["Batch Transfer", "SQL Access", "Data Products",
                "Semantic & Metric Layer", "Analysts", "Business Users"],
        notes=[
            "The raw zone is not skipped. Device payloads are kept exactly as received, "
            "because sensors fail in surprising ways and the evidence is the payload.",
            "Curated holds only the signals operations reacts to; everything else stays "
            "raw, cheap, and unmodelled.",
            "The consumer is a control system, so the interface is REST, not SQL. A "
            "dashboard would be the wrong shape for this answer.",
        ],
    ),
    "secure-data-sharing": dict(
        title="Secure data sharing with partners",
        lead=("A boundary flow. Data is replicated from the operational systems, conformed "
              "enough to be contractually safe, and shared outward with a partner "
              "organisation. The hard part is not the pipeline, it is what happens after "
              "the data leaves."),
        unused=["Streaming", "Curated", "Data Products", "Analysts", "Business Users",
                "Semantic & Metric Layer"],
        notes=[
            "Only Raw and Standardized are used: the partner receives a contracted shape, "
            "not an internal mart shaped for your own reporting.",
            "Secure Data Sharing replaces SQL Access. The boundary here is a permission "
            "grant and a contract, not a query engine.",
            "Lifecycle, Retention & Deletion and Audit & Compliance Reporting are on the "
            "path because a shared dataset keeps carrying obligations once it is outside "
            "your control.",
        ],
    ),
}

ORDER = ["finance-reporting", "customer-360", "ml-and-ai", "federated-reporting",
         "realtime-alerts", "iot-telemetry", "self-service-bi", "secure-data-sharing",
         "compliance-retention"]


def page_text(slug):
    e = bd.EXAMPLES[slug]
    p = PROSE[slug]

    stage_rows = []
    for n, card in enumerate(e["overview"], 1):
        stage = bd.COLS[bd.CELL[card][0]][0].split(" · ")[1].title()
        stage_rows.append(f"| {n} | {stage} | {card} | "
                          f"[{stage}](../{STAGE_GUIDE[stage][3:]}) |")

    cap_rows = []
    for n, card in enumerate(e["detailed"], 1):
        x, y = coords[card]
        pl = plane(x, y)
        name = card.split("#")[0]
        cap_rows.append(f"| {n} | {name} | [{pl}]({GUIDE[pl]}) | {PLAIN[name]} |")

    body = [f"# {p['title']}", "", p["lead"], ""]
    if "diagram" in p:
        body += [f"See also: {p['diagram']}", ""]
    body += [f"![{p['title']}, six stages](img/{slug}-overview.png)", "",
             "## Why this flow is in the catalogue", ""]
    body += [f"- {w}" for w in WHY[slug]]
    body += ["", "## Stages", "",
             "| Step | Stage | Box | Guide chapter |",
             "| --- | --- | --- | --- |", *stage_rows, "",
             f"![{p['title']}, capability inventory](img/{slug}-inventory.png)", "",
             "## Capabilities", "",
             "| Step | Capability | Plane | In plain terms |",
             "| --- | --- | --- | --- |", *cap_rows, "",
             "## Not used by this flow", "",
             "Not a judgement: these capabilities are simply not on the path. "
             + ", ".join(p["unused"]) + ".", "",
             "## Notes", ""]
    body += [f"- {n}" for n in p["notes"]]
    if "followup" in p:
        body += ["", "## Where this flow continues", "", p["followup"]]
    body += ["", "---", "",
             "Back to [worked flows](README.md) and the "
             "[reference architecture](../README.md).", ""]

    return "\n".join(body)


def matrix_rows():
    return "\n".join(
    "| "
    + f"[{PROSE[slug]['title']}]({slug}.md)"
    + "".join(
        " | " + (", ".join(c for c in bd.EXAMPLES[slug]["overview"]
                           if bd.CELL[c][0] == i) or "—")
        for i in range(len(bd.COLS))
    )
    + " |"
    for slug in ORDER
)

def index_text():
    rows = matrix_rows()
    return f"""# Worked Flows

Nine flows traced end to end through the architecture at both altitudes. The point is not
the diagrams on their own; it is that the same flow lands on the same boxes twice, once
at stage level and once at capability level.

| Image | What it shows |
| --- | --- |
| `*-overview.png` | which of the six stages the flow touches |
| `*-inventory.png` | which capabilities it uses |

Teal means on the path, with a step number. Faded means the capability exists in the
reference architecture but this flow does not use it.

## The flows

Every flow below uses a different mix of the Storage, Processing and Serving columns.

| Flow | Sources | Integration | Storage | Processing | Serving | Consumption |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## How to read one

Each page has three parts: why the flow is in the catalogue, the stages it uses, and the
capabilities it needs, each with a plain-language line and a link to the guide chapter
that explains it properly. The stage table answers "where does this flow go"; the
capability table answers "what has to exist for it to work". Together they are the
checklist an implementation team actually plans against.

Start with the flow closest to your own problem, read it top to bottom, then follow the
chapter links for the capabilities you do not have yet.

A data product is **one publish mode among six**, not a mandatory last step. Two of the
nine flows publish one. The others serve through SQL access, REST and GraphQL APIs,
federated access, or a sharing grant, because a training job, an alert consumer and a
partner organisation are different audiences with different contracts. If every flow ended
in a data product, the diagram would be describing a choke point instead of a choice.

An em dash in the matrix is a stage the flow genuinely skips, not a gap in the
documentation. The federated flow stores nothing, which is the whole point of it.

## Why the split into two altitudes

This follows the shape of the reference architectures published by
[a16z](https://a16z.com/emerging-architectures-for-modern-data-infrastructure/). They
publish one unified stack, plus a separate machine learning stack, because the ML tool
chain is complex and increasingly independent. We keep the same idea with two altitudes
instead of two stacks: one picture to agree on the shape of the pipeline, one to plan the
work inside each stage, and worked flows to prove both agree.

## ML and AI coverage

The inventory models the ML tool chain as a fifth band: feature store, experiment
tracking, model registry, model serving, vector index, and evaluation and drift. The
[ML and AI view](../diagrams/mlAiOverview.png) draws how those boxes connect, which the
band cannot show. Embedding generation and retrieval pipelines are the thinnest part of
this coverage; the a16z
[machine learning reference architecture](https://a16z.com/emerging-architectures-for-modern-data-infrastructure/)
is the better source there.
"""
CHAPTERS = {
    "01": ("guide/01-data-sources.md", "Data Sources"),
    "02": ("guide/02-integration-plane.md", "Integration Plane"),
    "03": ("guide/03-enterprise-platform.md", "Enterprise Platform"),
    "04": ("guide/04-serving-access.md", "Serving & Data Products"),
    "05": ("guide/05-data-products.md", "Serving & Data Products"),
    "06": ("guide/06-consumption.md", "Data Consumption"),
    "07": ("guide/07-metadata-knowledge.md", "Metadata & Knowledge"),
    "08": ("guide/08-governance-trust.md", "Governance & Trust"),
    "09": ("guide/09-control-plane.md", "Control Plane"),
    "10": ("guide/10-platform-engineering.md", "Platform Engineering"),
}


def guide_flows(chapter):
    """Flows that exercise a chapter's plane, most involved first."""
    if chapter == "05":
        return [s for s in ORDER if "Data Products" in bd.EXAMPLES[s]["overview"]]
    target = CHAPTERS[chapter][1]
    scored = []
    for slug in ORDER:
        hits = sum(1 for c in bd.EXAMPLES[slug]["detailed"]
                   if plane(*coords[c]) == target)
        if hits:
            scored.append((hits, slug))
    scored.sort(key=lambda t: (-t[0], ORDER.index(t[1])))
    return [slug for _, slug in scored[:3]]


def build_all():
    out = {f"examples/{slug}.md": page_text(slug) for slug in ORDER}
    out["examples/README.md"] = index_text()
    for chapter, (path, _) in CHAPTERS.items():
        body = (REPO / path).read_text()
        body = re.sub(r"\n<!-- flows:start -->.*?<!-- flows:end -->\n", "\n", body, flags=re.S).rstrip("\n")
        block = ["", "", "<!-- flows:start -->", "",
                 "## Worked Flows That Use This Stage", ""]
        for slug in guide_flows(chapter):
            tag = bd.EXAMPLES[slug]["tagline"]
            block.append(f"- [{PROSE[slug]['title']}](../examples/{slug}.md) — {tag}.")
        block += ["", "See [Worked Flows](../examples/README.md) for the full catalogue.",
                  "", "<!-- flows:end -->", ""]
        out[path] = body + "\n".join(block)
    return out