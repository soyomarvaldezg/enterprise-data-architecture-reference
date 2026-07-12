# 6. Data Consumption

## In Plain Language

Data consumption is about **who uses data, what systems use it, through which channels, and for what purpose**. The platform should provide different access patterns for different consumers rather than forcing everyone through the same interface.

A business user needing a dashboard doesn't need the same experience as a data scientist training a model or an application doing real-time fraud detection. Matching the access pattern to the consumer's needs is what makes a platform actually usable.

---

## The Analogy: A Library Serving Different Readers

Think of data consumption as a **public library serving different types of visitors**:

| Library Visitor                          | Data Consumer Equivalent | What They Need                                                                                             |
| ---------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Casual reader browsing bestsellers       | Business User            | Trusted dashboards, simple reports, business terminology — no schema knowledge required                    |
| Student researching a topic              | Analyst                  | SQL access, curated datasets, semantic models, ad-hoc exploration with lineage                             |
| PhD candidate analyzing raw archives     | Data Scientist           | Historical detail, experimentation environments, reproducible training datasets, point-in-time correctness |
| Software developer building an app       | ML Engineer / App Team   | Production-grade APIs, consistent training/serving data, low latency, versioned inputs                     |
| Book club getting a curated reading list | Embedded Analytics       | Pre-built visualizations integrated into another application                                               |
| Inter-library loan partner               | Partner / Third-Party    | Governed data sharing with clear scope, purpose, and expiration                                            |

A library doesn't force the casual reader to navigate the archival catalog system, and it doesn't give the PhD candidate only the bestseller shelf. **Different consumers need different interfaces.**

---

## What It Does

### 7.1 Consumers — Who Uses Data

| Consumer Type         | Typical Needs                                                                                                                  | Access Patterns                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Business Users**    | Trusted metrics, dashboards, reports, simple exploration, business terminology                                                 | Pre-built reports, self-service BI, semantic query interfaces                       |
| **Analysts**          | SQL access, curated datasets, semantic models, ad-hoc exploration, reproducible calculations                                   | Direct SQL, notebook environments, BI tools with governed datasets                  |
| **Data Scientists**   | Historical data, detailed features, experimentation environments, controlled sensitive data access, reproducible training data | Feature stores, sandbox environments, batch exports, point-in-time correct datasets |
| **ML Engineers**      | Production-grade interfaces, consistent training/serving data, low latency where needed, versioned inputs, monitoring          | APIs, feature stores, streaming endpoints, model serving infrastructure             |
| **Application Teams** | Operational data through APIs, events, search indexes, shared datasets with strong availability/latency commitments            | REST/GraphQL APIs, event streams, search indexes, materialized views                |

### 7.2 Applications — Systems That Consume Data

| Application Type             | Examples                                                                         | Key Requirements                                                    |
| ---------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Operational Applications** | Customer service apps, pricing engines, recommendation services, fraud detection | Low latency, high availability, real-time or near-real-time data    |
| **Downstream Systems**       | Finance systems, marketing platforms, planning systems, regulatory reporting     | Reliable delivery, audit trails, scheduled or event-driven updates  |
| **Embedded Analytics**       | Dashboards/metrics integrated into other applications                            | Tenant isolation, performance controls, consistent authorization    |
| **Partner Applications**     | Business partner systems consuming governed enterprise data                      | Secure sharing, clear data scope, usage restrictions, audit logging |
| **Third-Party Applications** | Externally managed products receiving data                                       | API contracts, rate limiting, versioning, deprecation policies      |

### 7.3 Channels — How Data Reaches Consumers

| Channel                | What It Is                                                         | Considerations                                                 |
| ---------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| **APIs**               | Programmatic interfaces for controlled access                      | Authentication, rate limiting, versioning, pagination          |
| **Partners**           | Formal business-to-business distribution                           | Contracts, data scope, allowed purpose, expiration, revocation |
| **Public Data**        | Intentionally published for unrestricted/broadly permitted use     | Still needs ownership, licensing, versioning, privacy review   |
| **External Consumers** | Customers, regulators, vendors, researchers outside the enterprise | Security boundaries, compliance requirements, audit trails     |

### 7.4 Consumption Patterns — What People Do With Data

| Pattern                               | Description                                                                                    | Example Use Cases                                              |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Analytics & Reporting**             | Standard BI, dashboards, scheduled reports, regulatory reporting                               | Monthly sales report, executive dashboard, compliance filing   |
| **Advanced Analytics & Data Science** | Statistical analysis, forecasting, experimentation, optimization, model development            | Churn prediction, demand forecasting, A/B test analysis        |
| **Embedded Analytics**                | Analytics integrated into operational applications or customer experiences                     | In-app recommendations, customer health scores in CRM          |
| **Self-Service Analytics**            | Authorized users discover and analyze governed data without central team building every output | Marketing analyst exploring campaign performance independently |

**Self-service does not mean uncontrolled access.** It requires strong semantics, metadata, quality enforcement, and policy — otherwise it becomes chaos.

---

## When You Need It

You're designing consumption whenever you:

- **Onboard a new consumer type** — e.g., adding ML engineers who need feature stores
- **Build a new application** that depends on platform data
- **Enable self-service analytics** for business teams
- **Share data with external partners** or publish public datasets
- **Embed analytics** into an operational application
- **Resolve conflicting access patterns** — "why can't the data science team get the same data the dashboard uses?"
- **Plan capacity** — different consumption patterns have different resource profiles

---

## Why It Matters

**Consumption is where value is realized.** All the integration, processing, and governance in the world doesn't matter if people can't get the data they need in the form they need it.

Getting consumption right means:

- **Right tool for the job** — business users get dashboards, scientists get notebooks, apps get APIs
- **Appropriate latency** — operational apps get real-time data; monthly reports don't need streaming
- **Security at the right level** — row-level security for sales reps, full access for auditors
- **Self-service without chaos** — governed discovery prevents shadow IT and duplicate effort
- **Scalable support** — different consumer types have different support expectations
- **Measurable value** — you can track which data products are actually used and by whom

---

## Key Terms

| Term                          | Simple Definition                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Consumer**                  | A person or system that uses data from the platform                                                   |
| **Self-Service Analytics**    | Authorized users exploring governed data independently without central team involvement               |
| **Embedded Analytics**        | Dashboards, metrics, or visualizations integrated directly into another application                   |
| **Feature Store**             | A system providing consistent, versioned features for both training and serving ML models             |
| **Point-in-Time Correctness** | Ensuring training data reflects what was known at the time, not future information (prevents leakage) |
| **Tenant Isolation**          | Ensuring one consumer's data and queries don't leak into another's (critical for embedded analytics)  |
| **Shadow IT**                 | Unsanctioned data pipelines or analyses built outside the governed platform                           |
| **Consumption Pattern**       | The way a consumer interacts with data (analytics, ML, operational, self-service)                     |

---

## Common Pitfalls

- **One-size-fits-all access** — forcing data scientists to use dashboards or business users to write SQL
- **No self-service guardrails** — "self-service" without governance becomes duplicate effort and conflicting definitions
- **Ignoring latency requirements** — giving an operational app batch data when it needs real-time
- **No consumption tracking** — you can't improve what you don't measure; know which assets are actually used
- **Treating all consumers equally** — critical operational apps need stronger SLAs than experimental analyses
- **Missing deprecation communication** — retiring an API or dataset without notifying dependent consumers
- **Over-restricting access** — excessive controls push users to find workarounds; balance security with usability
