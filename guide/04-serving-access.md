# 4. Serving & Access Plane

## In Plain Language

The serving and access plane is the **interface layer** between your data platform and the people/systems that need data. It has three responsibilities:

1. **Define business meaning** — what do terms like "revenue," "active customer," or "churn" actually mean?
2. **Make that meaning executable** — turn human definitions into machine-consumable models
3. **Expose controlled access** — provide APIs, SQL endpoints, and sharing mechanisms so consumers can get data safely

It separates consumers from physical storage details. A business user asking for "Q3 revenue by region" shouldn't need to know which tables to join or how currency conversion works.

---

## The Analogy: A Restaurant's Menu and Service Counter

Think of the serving and access plane as a **restaurant's front-of-house operations**:

| Restaurant Concept                                        | Serving & Access Equivalent                                                |
| --------------------------------------------------------- | -------------------------------------------------------------------------- |
| Menu descriptions ("pan-seared salmon with lemon butter") | Business Semantics — clear definitions of what each item means             |
| Kitchen recipes and prep standards                        | Semantic Services — turning menu descriptions into executable instructions |
| Waiters, takeout counter, delivery app                    | Access Services — different ways customers get their food                  |
| "Gluten-free," "spicy level," "allergen info"             | Dimensions, hierarchies, filters — ways to customize what you get          |
| Consistent taste across locations                         | Metric models — same calculation regardless of who asks                    |

A restaurant doesn't send customers into the kitchen to figure out what's available. The menu defines options clearly, the kitchen knows how to prepare them consistently, and the service staff delivers them through the right channel (dine-in, takeout, delivery).

**Data platforms work the same way.** Consumers shouldn't need to understand physical table structures. They should ask in business terms and get consistent, governed answers.

---

## What It Does

### 5.1 Business Semantics — Defining Meaning

| Concept                      | What It Is                                 | Example                                                                                       |
| ---------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Business Metrics & KPIs**  | Formulas for important measures            | Revenue = sum of completed orders minus returns; Active Customer = transacted in last 90 days |
| **Business Definitions**     | Agreed meanings of important terms         | "Customer" = entity with an active account AND at least one transaction in 12 months          |
| **Dimensions & Hierarchies** | Perspectives for analysis and their levels | Geography: Country → Region → City → Store; Product: Category → Subcategory → SKU             |
| **Business Rules**           | Explicit enterprise logic                  | Cancelled orders don't contribute to revenue; inventory below zero is invalid                 |

A metric name without its formula, grain, time behavior, filters, and owner is **not an adequate definition**.

### 5.2 Context & Semantic Services — Making Meaning Executable

| Service                             | What It Does                                                                                  | Why It Matters                                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Semantic Models**                 | Connect physical data structures to business concepts (entities, measures, dimensions, joins) | Different tools calculate the same metric consistently                                                    |
| **Business Ontology**               | Models business concepts and their formal relationships                                       | Goes beyond a glossary — defines how concepts relate (customer _places_ order, order _contains_ products) |
| **Metric Models**                   | Reusable, executable measure definitions with valid dimensions, aggregation rules, versioning | Prevents every analyst from rebuilding the same KPI differently                                           |
| **Semantic Query APIs**             | Let consumers request data using business concepts, not table names                           | "Revenue by region" instead of "SELECT SUM(amount) FROM fact_orders JOIN dim_geo..."                      |
| **Metric Calculation & Resolution** | Selects and executes the correct metric definition based on context                           | Resolves which version, dimensions, aggregation method, and source apply                                  |

### 5.3 Access Services — How Consumers Get Data

| Access Method             | What It Is                                                                 | Best For                                                        | Key Controls Needed                                                             |
| ------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **SQL Access**            | Direct query access for analysts, engineers, BI tools                      | Ad-hoc exploration, complex analysis                            | Authentication, authorization, row/column-level security, masking, query quotas |
| **REST APIs**             | Resource-oriented HTTP interfaces                                          | Operational applications, controlled external access            | Versioning, rate limiting, pagination, error contracts, deprecation policies    |
| **GraphQL APIs**          | Typed schema letting consumers request specific fields                     | Reducing over-fetching when consumers need varied subsets       | Query complexity limits, authorization, performance controls                    |
| **Data Virtualization**   | Logical view across systems without physically moving data                 | Reducing copying when real-time cross-system queries are needed | Source latency awareness, query-cost management, security complexity            |
| **Secure Data Sharing**   | Governed access without distributing uncontrolled copies (platform-native) | Internal or external sharing with revocation and audit          | Provider/consumer scope, allowed purpose, expiration, audit requirements        |
| **Data Exchange**         | Controlled environment for publishing and discovering/subscribing to data  | Internal or external data marketplace scenarios                 | Discovery, subscription management, usage tracking                              |
| **Federated Data Access** | Consistent access model across independently managed systems/domains       | Multi-domain or multi-organization environments                 | Coordinated policies, identity, discovery conventions                           |

---

## When You Need It

You're designing serving and access whenever you:

- **Standardize how metrics are calculated** across dashboards, reports, and APIs
- **Build self-service analytics** so business users don't need engineering help for every question
- **Expose data to external partners** or third-party applications
- **Optimize query performance** for specific consumer patterns
- **Enforce row-level or column-level security** (e.g., sales reps see only their territory)
- **Deprecate old interfaces** while migrating consumers to new ones
- **Resolve conflicting definitions** ("why does Finance's revenue differ from Sales' revenue?")

---

## Why It Matters

**Serving and access is where data becomes useful.** Without it, you have well-processed data sitting in databases that no one can safely or efficiently use.

Getting it right means:

- **Consistency** — everyone calculates "revenue" the same way, eliminating conflicting reports
- **Self-service** — authorized users find and analyze data without bottlenecking on central teams
- **Security** — sensitive data is masked, restricted, or audited appropriately
- **Performance** — consumers get answers fast through optimized interfaces
- **Flexibility** — different consumers get data through the interface that suits them (SQL, API, semantic query)
- **Trust** — clear definitions and lineage let consumers understand what they're looking at

---

## Key Terms

| Term                      | Simple Definition                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Business Semantics**    | The agreed-upon meaning of business terms, metrics, and rules                                  |
| **Semantic Model**        | A layer connecting physical data structures to business concepts                               |
| **Ontology**              | A formal model of business concepts and their relationships (beyond just definitions)          |
| **Metric Model**          | A reusable, executable definition of a measure with its valid dimensions and aggregation rules |
| **Dimension**             | A perspective through which metrics can be analyzed (customer, product, time, geography)       |
| **Hierarchy**             | Levels within a dimension defining valid aggregation paths (Country → Region → City)           |
| **Data Virtualization**   | Querying data across systems without physically copying it                                     |
| **Federation**            | Coordinated access across independently managed systems or domains                             |
| **Row-Level Security**    | Restricting which rows a user can see based on their attributes                                |
| **Column-Level Security** | Restricting which columns/fields a user can see                                                |
| **Semantic Query API**    | An interface letting consumers request data using business concepts instead of table names     |

---

## Common Pitfalls

- **Letting every team define metrics independently** — leads to conflicting numbers and lost trust
- **Exposing raw tables directly to business users** — they'll join incorrectly, misinterpret fields, and get wrong answers
- **Ignoring query performance** — unoptimized SQL access can bring down the platform during peak usage
- **Treating virtualization as free** — it reduces copying but adds latency, complexity, and source dependency
- **No deprecation strategy** — old APIs and views accumulate; plan for sunsetting with consumer migration paths
- **Missing semantic layer** — without it, every dashboard rebuilds the same logic differently
- **Over-granular access controls** — too many custom rules become unmaintainable; aim for attribute-based policies
