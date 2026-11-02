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
| The shelf itself: plated portions, priced       | Serving Views — views and precomputed results built for consumers |
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
| **Serving Views**| Views, materialized views, authorized views, application-ready data               | Adapted to consumer performance and access requirements | Derived representations, not new authoritative records; may intentionally duplicate data       |

**Relationship to Bronze/Silver/Gold:** There's a rough correspondence (Raw ≈ Bronze, Standardized ≈ Silver, Curated ≈ Gold), but those names aren't universal standards. What matters is the _responsibility_ of each zone, not its label. Serving adds an explicit consumer-optimized layer beyond the traditional three.

**What actually lives in the serving layer.** Bronze/silver/gold usually ends with facts and dimensions in curated (gold), and that is where the modelling stops. Serving is not a fourth medallion stage; it is the delivery layer built on top of gold, and what sits in it is views:

- A **logical view** is a saved query. It costs nothing to store and is evaluated every time someone reads it.
- A **materialized view** stores the results and refreshes them in the background. It exists so a dashboard does not recompute a year of facts on every page load, and so the warehouse bill does not grow with refresh frequency.
- An **authorized view** exposes a filtered subset without granting access to the underlying tables. In practice this is how most row-level and column-level security is delivered, because the consumer never touches the base table.

Every warehouse implements these under slightly different names, and some charge differently for them, but the responsibilities are the same. If your curated zone already holds a star schema, the serving layer is where those facts and dimensions become something a consumer can query cheaply and only see what they are allowed to see.

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
| **Serving Views**     | Views, materialized views and authorized views built for a consumer's access pattern        |
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

<!-- flows:start -->

## Worked Flows That Use This Stage

- [ML and AI features from governed data](../examples/ml-and-ai.md) — batch features for models, stopping where the reference stops.
- [Finance reporting from an ERP and CRM](../examples/finance-reporting.md) — batch, ERP and CRM, published as a governed data product.
- [Customer 360 from operational systems](../examples/customer-360.md) — streaming, one identity per customer, served inside an app.

See [Worked Flows](../examples/README.md) for the full catalogue.

<!-- flows:end -->
