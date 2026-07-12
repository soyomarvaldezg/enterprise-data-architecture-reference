# 7. Metadata & Knowledge Plane

## In Plain Language

Metadata is **data about data** — it describes where data came from, what it means, who owns it, how it changed, and how it may be used. Without metadata, your data platform is a warehouse full of unlabeled boxes. You have stuff, but no one knows what's inside, where it came from, or whether it's safe to use.

The metadata and knowledge plane transforms disconnected technical assets into an **understandable enterprise information environment**. It answers questions like: "What does this column mean?", "Where did this number come from?", "Who can I ask about this dataset?", and "What breaks if I change this table?"

---

## The Analogy: A Library's Catalog System

Think of metadata as a **library's catalog, card system, and librarian knowledge**:

| Library Concept                                      | Metadata Equivalent                                                             |
| ---------------------------------------------------- | ------------------------------------------------------------------------------- |
| Card catalog / online catalog                        | Enterprise Catalog — inventory of all data assets                               |
| "This book was cited by..." / "Cites these works..." | Data Lineage — how data flows and transforms from source to consumption         |
| Subject headings, search index                       | Data Discovery — helping people find relevant assets                            |
| Dictionary of terms in the back of a textbook        | Business Glossary — agreed definitions of business terms                        |
| "Restricted section," age ratings                    | Data Classification — sensitivity labels driving access controls                |
| Librarian recommending related books                 | Active Metadata — metadata that triggers actions (not just documentation)       |
| Cross-references between topics                      | Knowledge Graph — connecting business terms, assets, owners, policies, products |
| Edition numbers, ISBN registry                       | Schema & Interface Registry — versioned technical contracts                     |

A library without a catalog is just a room full of books. You might eventually find what you need, but it takes forever and you'll miss things. **Metadata is the catalog that makes data findable, understandable, and trustworthy.**

---

## What It Does

| Capability                                   | What It Is                                                                                                                                                     | Why It Matters                                                                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Enterprise Catalog**                       | Inventory of data assets (tables, files, streams, APIs, reports, metrics, models, data products) with ownership, descriptions, classifications, lineage, usage | People can discover what exists and understand what they're looking at                                                               |
| **Data Lineage**                             | Shows how data moves and transforms from source to consumption, including transformations (not just system-to-system connections)                              | Root-cause analysis, impact analysis, compliance, change planning, consumer trust                                                    |
| **Data Discovery**                           | Helps consumers find relevant assets through search, tags, domains, popularity, certifications, relationships, usage history                                   | Reduces time-to-insight; prevents duplicate effort                                                                                   |
| **Business Glossary**                        | Defines agreed business terms and connects them to data assets, metrics, policies, and owners                                                                  | Eliminates ambiguity — "active customer" means the same thing everywhere                                                             |
| **Data Classification**                      | Identifies sensitivity or usage categories (public, internal, confidential, restricted, PII, financial)                                                        | Drives access controls, masking, encryption, retention policies                                                                      |
| **Active Metadata**                          | Metadata that triggers actions rather than remaining passive documentation                                                                                     | A schema change triggers validation; sensitivity classification applies masking; failed quality rules create incidents               |
| **Knowledge Graph & Semantic Relationships** | Connects business terms, data assets, owners, domains, metrics, policies, entities, products, and lineage relationships in a queryable model                   | Makes relationships between technical and business concepts explorable                                                               |
| **Schema & Interface Registry**              | Stores versioned contracts for events, messages, files, APIs, datasets                                                                                         | Supports technical compatibility and contract enforcement (different from catalog — registry is for machines, catalog is for people) |

### Catalog vs. Registry — What's the Difference?

| Aspect       | Catalog                                                   | Registry                                             |
| ------------ | --------------------------------------------------------- | ---------------------------------------------------- |
| **Audience** | People discovering and understanding assets               | Systems enforcing compatibility                      |
| **Purpose**  | Discovery, documentation, trust                           | Contract validation, version management              |
| **Content**  | Descriptions, owners, lineage, usage                      | Schemas, versions, compatibility rules               |
| **Example**  | "This table contains customer orders, owned by Sales Ops" | "Event schema v2.1 is backward-compatible with v2.0" |

---

## When You Need It

You're investing in metadata whenever you:

- **New hires can't find data** — onboarding takes weeks because no one knows what exists
- **"What does this column mean?"** is a common question — tribal knowledge hasn't been captured
- **A schema change breaks downstream consumers** — no one knew who depended on that field
- **Compliance audits require data lineage** — you can't prove where regulated data came from
- **Duplicate datasets proliferate** — three teams built similar tables because they couldn't find each other's work
- **Sensitive data leaks** — classification wasn't applied consistently
- **Schema changes cause silent breaking changes** — no compatibility checking before deployment

---

## Why It Matters

**Metadata is the difference between a data platform and a data swamp.** Without it:

- **Discovery fails** — people rebuild what already exists because they can't find it
- **Trust erodes** — consumers don't know where data came from or whether it's reliable
- **Changes are dangerous** — no one knows what breaks when you modify a table
- **Compliance is painful** — auditors ask for lineage and you scramble to reconstruct it manually
- **Onboarding is slow** — new team members depend entirely on tribal knowledge
- **Security gaps emerge** — sensitive data isn't classified, so access controls aren't applied

Getting metadata right means:

- **Findability** — people discover existing assets instead of rebuilding them
- **Understandability** — business terms are defined; technical structures are documented
- **Impact awareness** — you know what breaks before you make a change
- **Compliance readiness** — lineage, classification, and ownership are always current
- **Active governance** — metadata drives automated controls, not just passive documentation
- **Organizational memory** — knowledge survives personnel changes

---

## Key Terms

| Term                    | Simple Definition                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------- |
| **Metadata**            | Data about data — descriptions, ownership, lineage, classification, usage              |
| **Data Lineage**        | The path data takes from source to consumption, including transformations              |
| **Business Glossary**   | Agreed definitions of business terms connected to technical assets                     |
| **Data Classification** | Labeling data by sensitivity to drive security and access controls                     |
| **Active Metadata**     | Metadata that triggers automated actions (not just passive documentation)              |
| **Knowledge Graph**     | A model connecting business concepts, data assets, owners, policies, and relationships |
| **Schema Registry**     | A system storing versioned technical contracts for interfaces and datasets             |
| **Enterprise Catalog**  | An inventory of data assets with descriptions, ownership, and lineage                  |
| **Data Discovery**      | The capability to search and find relevant data assets                                 |
| **Tribal Knowledge**    | Information known only to individuals, not documented — a risk when people leave       |

---

## Common Pitfalls

- **Treating metadata as optional** — it's not documentation overhead; it's the foundation of usability
- **Manual metadata entry** — if people have to update it by hand, it will go stale; automate collection
- **Catalog without lineage** — knowing what exists isn't enough; you need to know where it came from
- **Glossary disconnected from assets** — definitions in a wiki that don't link to actual tables are useless
- **Passive metadata only** — if metadata doesn't trigger actions (masking, validation, alerts), it's just documentation
- **No ownership tracking** — metadata without owners becomes orphaned and unreliable
- **Confusing catalog and registry** — they serve different audiences; don't try to make one tool do both jobs poorly
