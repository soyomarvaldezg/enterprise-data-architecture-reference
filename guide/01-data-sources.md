# 1. Data Sources

## In Plain Language

Data sources are the places where data originates — the systems, devices, files, and services that produce or hold information your organization needs. The data platform doesn't own these systems; it connects to them safely, understands what they contain, and preserves their meaning when moving data elsewhere.

Think of data sources as **the wells and rivers in a water utility system**. Some are on your property (internal), some belong to neighbors or suppliers (external). You don't control how much rain falls or how deep the well is, but you do need to know where each source is, how reliable it is, and whether the water is safe to bring into your system.

---

## The Analogy: A City's Water Supply Network

Imagine you're responsible for supplying clean water to a city. Your job starts _before_ the treatment plant — you need to know:

- **Where does water come from?** Rivers, groundwater wells, reservoirs, rainwater collection
- **Who owns each source?** Municipal wells, private landowners, neighboring jurisdictions
- **How reliable is it?** Seasonal rivers dry up; wells can run low; rainfall is unpredictable
- **What quality issues exist?** Some sources have sediment, others have minerals, some are contaminated

You wouldn't blindly pump water from an unknown source into your treatment plant. You'd catalog each source, test its quality, understand its limits, and plan accordingly.

**Data sources work the same way.** Before data enters your platform, you need to know where it came from, who owns it, how often it changes, what format it's in, and whether it's trustworthy.

---

## What It Does

Data sources represent the **origin points** of enterprise information. They fall into two broad categories:

### Internal Sources (systems your organization operates)

| Source Type           | Examples                                                                         | Key Questions                                                                                        |
| --------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Databases**         | Transactional DBs, document stores, key-value stores, legacy/mainframe databases | Is this the authoritative record? Can we extract changes incrementally? How much load can it handle? |
| **Applications**      | ERP, CRM, finance systems, HR platforms, custom operational apps                 | What interface is most stable — API, events, or direct database access?                              |
| **Files & Documents** | CSV, JSON, XML, Excel, Parquet, PDF exports                                      | How do we detect new files? Handle duplicates? Validate structure?                                   |
| **Unstructured Data** | Free text, images, audio, video, scanned documents, logs                         | What metadata describes this content? Who can access it? How long do we keep it?                     |
| **Messages & Events** | "Order created", "Payment authorized", "Customer updated"                        | Are events immutable? Do they carry enough context? What happens if delivery fails?                  |
| **IoT Devices**       | Sensors, machines, connected devices                                             | How do we handle out-of-order events? Device identity? Intermittent connectivity?                    |

### External / Cloud Sources (systems outside your direct control)

| Source Type            | Examples                                                        | Key Challenges                                               |
| ---------------------- | --------------------------------------------------------------- | ------------------------------------------------------------ |
| **SaaS Applications**  | Salesforce, Workday, Shopify, marketing platforms               | Vendor-controlled schemas, API rate limits, limited history  |
| **APIs**               | Partner APIs, public data services, payment gateways            | Rate limiting, versioning, authentication, pagination        |
| **External Databases** | Partner databases, subsidiary systems, vendor systems           | Security boundaries, ownership clarity, change communication |
| **External Files**     | Regulatory filings, partner exports, customer uploads           | Stronger validation needed — you don't control quality       |
| **Streaming Data**     | Market feeds, logistics events, social media streams            | Ownership rights, replay capability, delivery guarantees     |
| **Third-Party Data**   | Purchased datasets, public government data, industry benchmarks | Licensing terms, usage restrictions, expiration dates        |

---

## When You Need It

You're dealing with data sources whenever you:

- **Onboard a new system** — a new CRM, a partner integration, a sensor deployment
- **Migrate away from a legacy system** — understanding what data lives there and how to extract it
- **Add a new analytics use case** — identifying which sources contain the data you need
- **Respond to a data quality issue** — tracing bad data back to its origin
- **Negotiate a data-sharing agreement** — defining what can be extracted, how often, and under what conditions

---

## Why It Matters

**Garbage in, garbage out.** No amount of processing can fix data that was misunderstood at the source. Getting sources right means:

- **Trustworthy outputs** — consumers know where data came from and can assess its reliability
- **Reproducible pipelines** — if something breaks, you can replay from the source
- **Compliance** — you know which sources contain sensitive data and can apply appropriate controls
- **Cost efficiency** — you extract only what you need, in the right frequency, without overloading source systems
- **Resilience** — when a source changes or fails, you have a plan because you documented it upfront

A senior architecture principle: **every source should have a minimum contract** documenting its owner, extraction method, expected volume, schema, retention requirements, and failure/replay procedure. This turns ad-hoc connections into managed relationships.

---

## Key Terms

| Term                               | Simple Definition                                                                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authoritative System of Record** | The system considered the "single source of truth" for a particular piece of data                                                                                   |
| **CDC (Change Data Capture)**      | A technique that captures inserts, updates, and deletes from a database by reading its transaction log — like watching a diary instead of re-reading the whole book |
| **Schema**                         | The structure or shape of data — what fields exist, what types they are                                                                                             |
| **Idempotency**                    | The property that doing something multiple times produces the same result as doing it once — important for retries                                                  |
| **Event Immutability**             | Once an event happened, it can't be changed — you can add corrections, but the original record stays                                                                |
| **Data Classification**            | Labeling data by sensitivity (public, internal, confidential, restricted) to drive security controls                                                                |
| **Source Contract**                | A documented agreement about how a data source will be accessed, what to expect from it, and how failures are handled                                               |

---

## Common Pitfalls

- **Assuming all sources are equal** — a production transactional database has very different constraints than a monthly CSV export
- **Skipping source documentation** — "we'll figure it out later" becomes expensive when someone leaves or a system changes
- **Direct database access without approval** — querying a production database can slow down the business application running on it
- **Treating files as reliable contracts** — a file arriving doesn't mean its contents are correct; validate both structure and content
- **Ignoring external source volatility** — SaaS vendors change APIs without notice; build monitoring for schema drift
