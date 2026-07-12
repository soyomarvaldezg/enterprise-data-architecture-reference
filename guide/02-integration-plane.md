# 2. Data Integration Plane

## In Plain Language

The integration plane is the **transportation system** of your data platform. It answers three questions:

1. **When and how do we pick up data?** (ingestion patterns)
2. **What vehicle moves it?** (integration methods)
3. **What road does it travel on?** (connectivity)

Its job is reliable movement — getting data from point A to point B without losing, duplicating, or corrupting it. It should _not_ be where complex business logic hides; that belongs in the processing layer.

---

## The Analogy: A City's Transportation Network

Think of the integration plane as the **roads, railways, pipelines, and delivery services** that move goods across a city:

| Transportation Concept                  | Data Integration Equivalent                                                      |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| Scheduled freight trains                | Batch ingestion — large loads at predictable times                               |
| Express courier vans                    | Streaming — continuous, low-latency delivery                                     |
| Package consolidation centers           | Micro-batch — small groups processed frequently                                  |
| Moving companies tracking changes       | CDC — only moving what changed, not everything                                   |
| Phone calls / walk-in counters          | Request/response — ask and wait for an answer                                    |
| Domino effect triggers                  | Event-driven — one event sets off a chain reaction                               |
| Public roads, private highways, tunnels | VPN, peering, dedicated connectivity — different paths with different properties |

You wouldn't send a single urgent letter via freight train, and you wouldn't ship 10,000 tons of steel by courier van. **Choosing the right pattern matters.**

---

## What It Does

### 3.1 Ingestion Patterns — When and How We Pick Up Data

| Pattern                       | What It Is                                                   | When to Use It                                                 | Trade-offs                                                    |
| ----------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------- |
| **Batch**                     | Collect data over time, process as a group                   | Daily reports, historical backfills, sources that can't stream | Higher latency; simpler to implement and reprocess            |
| **Streaming**                 | Process data continuously as it arrives                      | Real-time dashboards, fraud detection, live monitoring         | Complex state management; ordering and replay concerns        |
| **Micro-batch**               | Small, frequent batches (e.g., every 30 seconds)             | Near-real-time needs without full streaming complexity         | Still batch semantics; lower latency than traditional batch   |
| **CDC (Change Data Capture)** | Capture only inserts, updates, deletes from source databases | Keeping a copy in sync with a live operational database        | Requires transaction log access; schema change handling       |
| **Request/Response**          | Consumer asks, provider answers synchronously                | Interactive lookups, validation checks                         | Creates temporal coupling; not scalable for bulk distribution |
| **Event-Driven**              | An event triggers an action downstream                       | Workflow automation, reactive systems, notifications           | Broader architectural style; not the same as event streaming  |

### 3.2 Integration Methods — What Vehicle Moves Data

| Method                                | What It Is                                                           | Best For                                                   |
| ------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Publish & Subscribe**               | Producers publish; consumers subscribe to topics they care about     | Decoupling many producers from many consumers              |
| **Event Streaming**                   | Durable, ordered stream of events that multiple consumers can replay | Analytics, event sourcing, independent consumer processing |
| **Replication / CDC**                 | Copying data state or changes from one system to another             | Synchronization, backup, read replicas                     |
| **Database Connectivity (JDBC/ODBC)** | Standard protocols for querying databases directly                   | Simple integrations; watch out for production load         |
| **File Transfer (FTP/SFTP)**          | Moving files between systems                                         | Legacy integrations, partner exchanges, bulk exports       |
| **Data Transfer Services**            | Managed services for moving large datasets                           | Bulk migration, cross-cloud transfers, initial loads       |

### 3.3 Connectivity — What Road Does Data Travel On

| Connectivity Type                                    | What It Is                                                        | When to Use It                                       |
| ---------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| **VPN**                                              | Encrypted tunnel between networks                                 | Cloud-to-on-premises, partner connections            |
| **Private Service Connectivity / Private Endpoints** | Services exposed through private network addresses                | Reducing public internet exposure                    |
| **Network Peering**                                  | Direct network routing between environments                       | High-throughput, low-latency private communication   |
| **Dedicated Private Connectivity**                   | Provider-managed dedicated circuit                                | Critical production workloads, high-volume transfers |
| **Secure Connectors**                                | Agent running inside trusted environment with outbound connection | When inbound access to a source is prohibited        |

---

## When You Need It

You're designing integration whenever you:

- **Connect a new data source** to your platform
- **Need fresher data** than your current batch pipeline provides
- **Multiple teams need the same data** independently
- **A source system is being decommissioned** and data must be migrated
- **Regulatory requirements demand audit trails** of data movement
- **Latency becomes a business problem** — "we need this in seconds, not hours"

---

## Why It Matters

**Integration is the bloodstream of your data platform.** If it fails, nothing else matters — no amount of processing or governance helps if data never arrives.

Getting integration right means:

- **Reliable delivery** — data arrives completely, correctly, and on time
- **Appropriate latency** — you're not over-engineering streaming when daily batch suffices
- **Resilience** — retries, dead-letter queues, and replay capabilities handle failures gracefully
- **Source protection** — you're not crashing production databases with aggressive queries
- **Decoupling** — producers and consumers evolve independently without breaking each other
- **Cost efficiency** — you're not paying for real-time streaming when hourly batch meets business needs

---

## Key Terms

| Term                            | Simple Definition                                                              |
| ------------------------------- | ------------------------------------------------------------------------------ |
| **Ingestion**                   | The act of bringing data into the platform from a source                       |
| **Batch**                       | Processing a bounded collection of data at scheduled intervals                 |
| **Streaming**                   | Processing unbounded data continuously as individual records arrive            |
| **Micro-batch**                 | Processing small, frequent batches as a compromise between batch and streaming |
| **CDC (Change Data Capture)**   | Capturing only the changes (inserts, updates, deletes) from a source system    |
| **Pub/Sub (Publish/Subscribe)** | A messaging pattern where producers publish to topics and consumers subscribe  |
| **Dead-Letter Queue (DLQ)**     | A holding area for messages that couldn't be processed after retries           |
| **Idempotency**                 | Doing something multiple times produces the same result as doing it once       |
| **Backpressure**                | Slowing down producers when consumers can't keep up                            |
| **Watermark**                   | A marker indicating how far behind "real time" the stream processing is        |
| **Replayability**               | The ability to re-consume events from a stream from a given point              |

---

## Common Pitfalls

- **Using streaming when batch would suffice** — streaming adds operational complexity; don't pay for it unless you need it
- **Hiding business logic in integration** — the integration plane should move data reliably, not transform it extensively
- **Ignoring backpressure** — if consumers can't keep up, producers will eventually fail or lose data
- **Assuming "exactly-once" delivery** — most systems guarantee "at-least-once"; design for duplicates
- **Direct database queries without load testing** — a new pipeline can accidentally take down a production system
- **No replay mechanism** — when something breaks, you need to be able to reprocess from a known point
- **Treating file arrival as data validity** — a file showing up doesn't mean its contents are correct
