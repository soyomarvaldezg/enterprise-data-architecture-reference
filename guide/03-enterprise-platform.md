# 3. Enterprise Data Platform

## In Plain Language

The enterprise data platform is the **central processing and storage environment** — where data lives, gets cleaned, transformed, organized, and prepared for use. It's the heart of the architecture.

It contains three interconnected concepts:

1. **Logical Data Zones** — different "rooms" where data sits at different stages of refinement
2. **Data Processing Services** — the tools and capabilities that change, validate, and enrich data
3. **Data Provisioning & Serving** — optimized outputs prepared for specific consumers

Not every dataset must pass through every zone. The path depends on the use case.

---

## The Analogy: A Food Processing Facility

Think of the enterprise data platform as a **food processing and distribution center**:

| Food Facility Concept                       | Data Platform Equivalent                                          |
| ------------------------------------------- | ----------------------------------------------------------------- |
| Receiving dock (raw ingredients arrive)     | Raw Zone — data preserved close to source form                    |
| Washing, sorting, standardizing stations    | Standardized Zone — cleansed, conformed data                      |
| Recipe preparation, packaging lines         | Curated Zone — analytics-ready, business-purpose data             |
| Ready-to-sell products on shelves           | Serving Zone — optimized for specific consumers                   |
| Kitchen equipment (ovens, mixers, slicers)  | Processing Services — transformation, enrichment, validation      |
| Pre-made meals, meal kits, bulk ingredients | Provisioning — published datasets, materialized views, data marts |

A restaurant doesn't send every ingredient through every station. Lettuce for a salad goes through washing but not cooking. Flour for bread goes through mixing and baking but not washing. **The path depends on the final product.**

Similarly, not every dataset needs to be fully curated. Some consumers need raw data for exploration. Others need pre-aggregated serving tables for dashboards.

---

## What It Does

### 4.1 Logical Data Zones — Where Data Sits at Different Stages

These are **logical boundaries**, not necessarily separate technologies. A zone can be implemented through schemas, databases, storage prefixes, catalog namespaces, or access-control boundaries.

| Zone             | What It Contains                                                                 | Purpose                                                | Key Characteristics                                                                           |
| ---------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Raw**          | Source data, external data, event data, unstructured data                        | Traceability, replay, recovery, reconciliation         | Preserves original values; minimal reinterpretation; still needs metadata and access controls |
| **Standardized** | Cleansed data, conformed data, master/reference data, business entities          | Consistent enterprise representations                  | Type normalization, field renaming, code mapping, deduplication, identifier standardization   |
| **Curated**      | Analytics-ready data, dimensional models, aggregated data, reporting datasets    | Organized for defined analytical/business purposes     | Clear grain, documented measures, tested business rules, stable ownership                     |
| **Serving**      | Operational data, query-optimized data, low-latency data, application-ready data | Adapted to consumer performance/interface requirements | May intentionally duplicate data; derived representations, not new authoritative records      |

**Relationship to Bronze/Silver/Gold:** There's a rough correspondence (Raw ≈ Bronze, Standardized ≈ Silver, Curated ≈ Gold), but those names aren't universal standards. What matters is the _responsibility_ of each zone, not its label. Serving adds an explicit consumer-optimized layer beyond the traditional three.

### 4.2 Data Processing Services — What the Platform Can Do

| Service                 | What It Does                                  | Example                                                                                  |
| ----------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Data Transformation** | Changes structure, meaning, or representation | Joining datasets, calculating fields, reshaping nested structures                        |
| **Batch Processing**    | Operates on bounded datasets                  | Scheduled transformations, historical reprocessing, large aggregations                   |
| **Stream Processing**   | Continuously transforms unbounded data        | Windowed aggregations, stateful joins, deduplication, sessionization                     |
| **Event Processing**    | Interprets and reacts to events               | Pattern detection, alert generation, workflow triggering, complex-event processing       |
| **Data Enrichment**     | Adds context from another source              | Adding customer segment, mapping product hierarchy, currency conversion                  |
| **Schema Evolution**    | Manages structural changes over time          | Adding/removing/renaming fields, changing types, compatibility policies                  |
| **Data Validation**     | Verifies data satisfies expectations          | Schema checks, required fields, allowed values, business rules, statistical expectations |

### 4.3 Data Provisioning & Serving — Optimized Outputs

| Provisioning Type      | What It Is                                          | When to Use It                                                                         |
| ---------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Published Datasets** | Governed outputs made available for reuse           | When data is intentionally consumable with owner, documentation, schema, access policy |
| **Materialized Views** | Precomputed query results stored for fast access    | Common aggregations, repeated joins, dashboard acceleration                            |
| **Data Marts**         | Subject-oriented analytical structures for a domain | Finance mart, sales mart, marketing mart — serves a particular use case                |
| **Search Indexes**     | Data organized for rapid retrieval                  | Full-text search, faceted search, entity lookup, catalog search                        |

---

## When You Need It

You're working in the enterprise platform whenever you:

- **Design how data flows** from raw ingestion to consumer-ready outputs
- **Define data quality gates** between zones (e.g., what must be true before data moves from standardized to curated)
- **Build reusable transformations** that multiple teams can depend on
- **Optimize query performance** for specific consumer patterns
- **Handle schema changes** without breaking downstream consumers
- **Decide whether to materialize or virtualize** a dataset

---

## Why It Matters

**The enterprise platform is where raw data becomes trusted information.** Getting it right means:

- **Traceability** — you can always trace a curated metric back to its raw source
- **Reusability** — standardized entities are built once, used many times
- **Performance** — serving-zone optimizations prevent slow dashboards and frustrated users
- **Governance enforcement** — zone boundaries are natural places to apply quality gates and access controls
- **Flexibility** — different consumers get data in the form they need without duplicating effort
- **Reproducibility** — batch idempotency and stream replay mean you can recreate any output

---

## Key Terms

| Term                  | Simple Definition                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------- |
| **Logical Zone**      | A conceptual boundary for data at a particular stage; not necessarily a separate system   |
| **Raw Data**          | Data preserved close to its source form, with minimal reinterpretation                    |
| **Standardized Data** | Data converted to consistent enterprise structures (types, naming, codes)                 |
| **Curated Data**      | Data organized for specific analytical or business purposes with clear grain and measures |
| **Serving Data**      | Data optimized for specific consumer access patterns (low latency, pre-aggregated)        |
| **Idempotency**       | Rerunning the same batch produces the same result without corruption or duplication       |
| **Grain**             | The level of detail in a dataset (e.g., per-order, per-day, per-customer)                 |
| **Dimensional Model** | A data model organized around facts (measures) and dimensions (contexts for analysis)     |
| **Materialized View** | A stored precomputed query result that improves performance for repeated access           |
| **Data Mart**         | A subject-oriented subset of data serving a specific domain or use case                   |
| **Schema Evolution**  | Managing changes to data structure over time while maintaining compatibility              |
| **Watermark**         | In stream processing, a marker indicating how far behind real-time the processing is      |

---

## Common Pitfalls

- **Forcing all data through all zones** — not every dataset needs full curation; match the path to the use case
- **Putting business logic in the wrong zone** — standardization should create reusable entities; curated applies use-case logic
- **Treating zones as physical systems** — zones are logical; you can implement multiple zones in one database with schemas or prefixes
- **Skipping validation between zones** — bad data propagates silently if you don't check at boundaries
- **Ignoring schema evolution** — sources change; your platform needs versioning and compatibility policies
- **Confusing curated datasets with data products** — a curated dataset is prepared data; a product adds ownership, contracts, SLAs, and lifecycle management
- **Over-materializing** — materialized views improve performance but add storage cost and staleness; use them judiciously
