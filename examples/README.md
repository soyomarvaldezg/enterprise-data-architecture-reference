# Worked Flows

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
| [Finance reporting from an ERP and CRM](finance-reporting.md) | Internal Systems | Batch Transfer | Raw, Standardized, Curated | Batch Transformation | Data Products | Business Users |
| [Customer 360 from operational systems](customer-360.md) | SaaS & Partners | Streaming | Raw, Standardized, Curated | Stream Processing | Data Products | Applications & Embedded |
| [ML and AI features from governed data](ml-and-ai.md) | Internal Systems, Files & Unstructured | Batch Transfer | Raw, Standardized, Curated | Data Enrichment | SQL Access | Data Scientists & ML |
| [Federated reporting without copying data](federated-reporting.md) | Public & Third-Party | APIs & Connectors | — | Data Validation | Federated Data Access | Analysts |
| [Real-time alerts from event streams](realtime-alerts.md) | Events & Streams | Streaming | Curated | Stream Processing | REST & GraphQL APIs | Applications & Embedded |
| [IoT telemetry from the factory floor](iot-telemetry.md) | IoT Devices | Micro-batch | Raw, Curated | Stream Processing, Schema Evolution | REST & GraphQL APIs | Operational Applications |
| [Self-service BI on a semantic layer](self-service-bi.md) | Internal Systems | CDC & Replication | Raw, Standardized, Curated, Serving Views, Materialized Views | Data Transformation | Semantic & Metric Layer | Analysts, Business Users |
| [Secure data sharing with partners](secure-data-sharing.md) | Internal Systems | CDC & Replication, Private Connectivity | Raw, Standardized | Data Validation | Secure Data Sharing | Partners & External |
| [Retention and audit](compliance-retention.md) | Internal Systems | Batch Transfer | Raw, Archive & Retention | Data Validation | SQL Access | Partners & External |

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
