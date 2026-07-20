# 5. Business Data Products

## In Plain Language

A business data product is a **trusted, reusable data offering aligned with a specific business outcome**. It's not just a table, dashboard, or pipeline — it's a managed service with an owner, consumers, contracts, quality objectives, and a lifecycle.

Think of it as the difference between **ingredients in a kitchen** and **a menu item at a restaurant**. Ingredients (curated datasets) are prepared and ready to use, but a menu item (data product) has a name, a description, a price, a chef responsible for it, consistency standards, and customers who expect it to be available when ordered.

The diagram shows five example data products: **Customer 360**, **Order Lifecycle**, **Inventory Availability**, **Financial Performance**, and **Marketing Attribution**. These are illustrations, not mandatory components. Every organization will have different data products based on its business.

The **Business Data Products** column represents a logical portfolio, not another storage or processing zone. The technical implementation of a product may span curated datasets, serving structures, semantic models, APIs, contracts, documentation, quality controls, and service-level objectives.

---

## The Analogy: A Restaurant Menu vs. Kitchen Prep Station

| Kitchen Concept                                        | Data Platform Equivalent                                       |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| Pre-chopped vegetables, pre-made sauces                | Curated datasets — prepared but not yet a complete offering    |
| Menu item with name, description, price, allergen info | Data product — defined offering with contract and expectations |
| Chef responsible for the dish                          | Domain owner — accountable for quality and availability        |
| Regulars who order it every week                       | Known consumers — people/systems depending on this product     |
| "Removed from menu" when ingredients run out             | Deprecation — planned retirement with consumer notification    |
| Consistent taste across visits                         | SLAs — freshness, quality, and availability guarantees         |

**Key distinction:** A curated dataset is technically prepared data. A data product is a _managed offering_ with ownership, contracts, service expectations, governance, and lifecycle. A curated dataset may become part of a data product, but they are not interchangeable.

---

## What It Does

### What Makes Something a Data Product

A legitimate data product must have **all** of these:

| Requirement                             | Why It Matters                                                   |
| --------------------------------------- | ---------------------------------------------------------------- |
| **Clearly identified domain owner**     | Someone accountable for quality, availability, and changes       |
| **Defined consumers**                   | You know who depends on it and can notify them of changes        |
| **Business purpose**                    | It solves a specific business problem, not just "available data" |
| **Published interface**                 | Schema or API contract that consumers can depend on              |
| **Business semantics**                  | Metrics, definitions, and rules are documented and governed      |
| **Data-quality objectives**             | Measurable thresholds for completeness, accuracy, timeliness     |
| **Freshness & availability objectives** | Consumers know how current the data is and when it's accessible  |
| **Security classification**             | Access controls match the sensitivity of the data                |
| **Lineage**                             | Consumers can trace data back to its sources                     |
| **Documentation**                       | Purpose, schema, refresh behavior, known limitations             |
| **Versioning**                          | Changes are tracked; breaking changes are communicated           |
| **Support & incident ownership**        | When something breaks, someone is on call                        |
| **Lifecycle & deprecation rules**       | Planned retirement with consumer migration paths                 |

### Example Data Products

| Data Product               | What It Provides                                                                                                         | Key Challenges                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Customer 360**           | Unified customer representation across systems (identity, contacts, transactions, preferences, consent)                  | Identity resolution, survivorship rules, consent management, source precedence           |
| **Order Lifecycle**        | Full progression of an order (Created → Confirmed → Paid → Fulfilled → Shipped → Delivered → Returned)                   | Authoritative events/timestamps, handling exceptions and reversals                       |
| **Inventory Availability** | Trusted representation of what can actually be sold (accounts for reservations, damaged units, in-transit, safety stock) | Low latency, reconciliation with physical inventory, real-time updates                   |
| **Financial Performance**  | Consistent finance measures (revenue, cost, margin, budget, forecast, variance)                                          | Strict reconciliation, period handling, currency rules, auditability                     |
| **Marketing Attribution**  | Connects marketing activity with customer behavior or revenue outcomes                                                   | Explicit attribution model (different models produce different answers from same events) |

---

## When You Need It

You're building a data product whenever you:

- **Multiple teams need the same data** with consistent definitions
- **Business outcomes depend on reliable data** (e.g., financial reporting, customer experience)
- **You want to reduce duplicate effort** — stop rebuilding the same customer view in every team
- **External partners or applications consume your data** — they need contracts, not ad-hoc access
- **You need accountability** — someone must own quality and availability, not just production
- **Data quality issues cause business impact** — formal SLOs drive investment in reliability

---

## Why It Matters

**Data products turn data from a technical asset into a business capability.** Without this concept, you get:

- **Conflicting definitions** — Finance and Sales report different "revenue" numbers
- **Duplicate effort** — five teams build their own customer view independently
- **No accountability** — when data is wrong, everyone points elsewhere
- **Fragile integrations** — consumers depend on undocumented tables that change without notice
- **Wasted trust** — business users stop believing the data after repeated inconsistencies

Getting data products right means:

- **Consistency** — one definition, one owner, one source of truth per business concept
- **Reliability** — SLAs and quality objectives drive operational discipline
- **Efficiency** — build once, reuse many times across the organization
- **Trust** — consumers know what to expect and who to contact when things break
- **Governance at scale** — policies apply to products, not individual tables

---

## Key Terms

| Term                                 | Simple Definition                                                                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Data Product**                     | A managed data offering with ownership, contracts, SLAs, and lifecycle — not just a table or dataset       |
| **Domain Owner**                     | The person/team accountable for a data product's quality, availability, and evolution                      |
| **Data Contract**                    | An agreement defining schema, quality thresholds, freshness, and compatibility rules                       |
| **SLO (Service Level Objective)**    | A measurable target for freshness, availability, or quality that a data product commits to                 |
| **Survivorship**                     | Rules determining which source "wins" when multiple systems provide conflicting data about the same entity |
| **Identity Resolution**              | Determining that records from different systems refer to the same real-world entity                        |
| **Attribution Model**                | A method for assigning credit to marketing touchpoints (first-touch, last-touch, multi-touch, etc.)        |
| **Deprecation**                      | Planned retirement of a data product with consumer notification and migration path                         |
| **Curated Dataset vs. Data Product** | Curated = prepared data; Product = curated data + ownership + contracts + SLAs + lifecycle                 |

---

## Common Pitfalls

- **Calling every table a "data product"** — if it doesn't have an owner, consumers, and SLAs, it's just a dataset
- **No deprecation process** — old products accumulate; consumers depend on things no one maintains
- **Owner is a team, not a person** — "the analytics team owns it" means no one specifically is accountable
- **Ignoring the hard parts** — Customer 360 isn't hard because of joins; it's hard because of identity, consent, and survivorship
- **Building products without consumers** — don't create a data product hoping someone will use it; start with a known need
- **Treating attribution as objective truth** — different models produce different answers; document which model you use and why
- **Missing versioning** — schema or logic changes break consumers silently; version and communicate
