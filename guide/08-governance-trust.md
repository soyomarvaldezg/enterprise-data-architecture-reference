# 8. Governance & Trust Plane

## In Plain Language

Governance defines **what must be true for enterprise data to be considered controlled, trustworthy, secure, and compliant**. It's not just approval meetings or documentation — it includes decision rights, ownership, standards, measurable policies, and accountability.

Trust is earned through consistent behavior over time. Governance is the system that makes consistent behavior possible at scale. Without it, every team makes their own rules, quality varies wildly, sensitive data leaks, and no one can prove compliance during an audit.

---

## The Analogy: A City's Building Codes and Health Inspections

Think of governance as a **city's building codes, health inspections, and regulatory framework**:

| City Regulation Concept                             | Governance Equivalent                                                                         |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Building codes (structural requirements)            | Data Governance — policies for ownership, naming, modeling, classification, access, retention |
| Health inspector checking restaurant kitchens       | Data Quality — verifying data is fit for its intended purpose                                 |
| Smoke detectors, fire alarms, sprinkler systems     | Data Observability — detecting abnormal behavior before it becomes a disaster                 |
| Business licenses, permits                          | Contract Policies — what a valid data contract must contain                                   |
| Restaurant grading (A, B, C)                        | Data Product Governance — certification levels for published products                         |
| Privacy laws, HIPAA, food safety regulations        | Data Privacy — what personal data may be collected, used and kept                            |
| Photo ID at the door, staff badges                  | Identity & Authentication — proving who a person or a service is                            |
| Locks on the doors, keys held by the manager        | Encryption & Key Management — scrambling data and controlling who holds the keys             |
| Blurring faces in CCTV footage                      | Data Masking & Tokenization — showing a redacted value instead of the real one               |
| Demolition permits, historical preservation rules   | Lifecycle, Retention & Deletion — how long data is kept and when it must be destroyed         |
| Automated code compliance checks in permit software | Policy as Code — executable, testable controls replacing manual reviews                       |
| Audit reports, inspection records                   | Audit & Compliance Reporting — evidence that controls operated correctly                      |

A city doesn't trust buildings because the architect said they're safe. It requires **inspections, codes, permits, and ongoing monitoring**. Data platforms need the same discipline.

---

## What It Does

| Capability                          | What It Is                                                                                                                         | Key Dimensions / Components                                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Data Governance**                 | Defines policies and standards for ownership, stewardship, naming, modeling, classification, publication, access, retention, usage | Federated where possible: central standards with domain-level accountability                                              |
| **Data Quality**                    | Defines whether data is fit for its intended purpose                                                                               | Completeness, accuracy, validity, uniqueness, consistency, timeliness, referential integrity                              |
| **Data Observability**              | Detects abnormal behavior in data systems                                                                                          | Freshness, volume, quality, schema, distribution changes, pipeline failures, missing partitions, unexpected null rates    |
| **Contract Policies**               | Defines what a valid data contract must contain                                                                                    | Required ownership, schema compatibility, freshness objectives, quality thresholds, deprecation notices, versioning rules |
| **Data Product Governance**         | Requirements for ownership, publication, operation, and retirement of data products                                                | Product owner, domain, lifecycle, SLOs, support, change management, consumer communication, certification                 |
| **Data Privacy**                    | What personal data may be collected, used, shared and kept                                                                        | Consent, purpose limitation, data minimization, subject access and erasure requests                                      |
| **Identity & Authentication**       | Proving who a person or a service is, once, and reusing that proof everywhere                                                      | Single sign-on, service accounts, workload identity, credential rotation                                                  |
| **Encryption & Key Management**     | Protecting data at rest and in transit, and controlling who holds the keys                                                        | Key custody (HSM or KMS), rotation, bring-your-own-key, envelope encryption                                               |
| **Data Masking & Tokenization**     | Showing a redacted value instead of the real one                                                                                  | Dynamic masking, static masking for non-production copies, tokenization, format-preserving pseudonyms                    |
| **Lifecycle, Retention & Deletion** | How long data is retained, when archived, when deleted, legal holds, deletion propagation to derived assets                        | Deletion is especially difficult when data has been copied into multiple downstream systems                               |
| **Policy as Code**                  | Converts written policies into executable and testable controls                                                                    | Prevent publishing unclassified datasets; require owners before production; reject incompatible schema changes            |
| **Audit & Compliance Reporting**    | Evidence showing who accessed data, which policy was applied, which change occurred, who approved publication                      | Who, what, when, why — traceable and verifiable                                                                           |

### Data Quality vs. Data Observability — What's the Difference?

| Aspect           | Data Quality                                    | Data Observability                                           |
| ---------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| **Focus**        | Does data satisfy _defined_ expectations?       | Is data behaving _normally_?                                 |
| **Approach**     | Tests against known rules                       | Detects anomalies and unexpected conditions                  |
| **Example**      | "Customer ID must not be null"                  | "Null rate jumped from 0.1% to 15% — something changed"      |
| **Scope**        | Known dimensions (completeness, accuracy, etc.) | Broader — includes patterns you didn't explicitly anticipate |
| **Relationship** | Quality is a subset of observability            | Observability encompasses quality plus anomaly detection     |

---

## When You Need It

You're investing in governance whenever you:

- **Regulated industry** — finance, healthcare, government require demonstrable controls
- **Data quality issues cause business impact** — wrong numbers lead to bad decisions
- **Multiple teams produce conflicting data** — no agreed standards or ownership
- **Sensitive data handling is inconsistent** — PII exposed in logs, unencrypted storage
- **Audits are painful** — reconstructing lineage and access history manually
- **Data products lack accountability** — no one owns quality or availability
- **Deletion requests aren't honored** — GDPR/CCPA compliance requires propagating deletions
- **Schema changes break consumers silently** — no compatibility enforcement

---

## Why It Matters

**Governance is the difference between a trusted platform and a liability.** Without it:

- **Bad decisions** — inaccurate data leads to wrong business choices
- **Regulatory fines** — non-compliance with privacy, financial, or industry regulations
- **Security breaches** — sensitive data exposed due to inconsistent controls
- **Lost trust** — business users stop believing the data after repeated errors
- **Operational chaos** — no one knows who owns what or how to handle incidents
- **Debt accumulation** — undocumented datasets, orphaned pipelines, stale contracts

Getting governance right means:

- **Trust at scale** — consumers believe the data because quality is measured and enforced
- **Compliance confidence** — audits are routine, not crises
- **Accountability** — every asset has an owner; every incident has a responder
- **Proactive detection** — observability catches problems before consumers notice
- **Automated enforcement** — policy as code prevents mistakes rather than detecting them after
- **Responsible data handling** — privacy, security, and retention are baked in, not bolted on

---

## Key Terms

| Term                              | Simple Definition                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Data Governance**               | Policies and standards for how data is owned, classified, accessed, and managed                    |
| **Data Quality**                  | Whether data is fit for its intended purpose across defined dimensions                             |
| **Data Observability**            | Detecting abnormal behavior in data systems beyond predefined quality rules                        |
| **Policy as Code**                | Executable, testable controls that enforce governance policies automatically                       |
| **Data Contract**                 | An agreement defining schema, quality, freshness, ownership, and compatibility rules               |
| **SLO (Service Level Objective)** | A measurable target for data product reliability (freshness, availability, quality)                |
| **Data Minimization**             | Collecting and retaining only the data necessary for a specific purpose                            |
| **Data Privacy**                   | Rules about what personal data may be collected, used and kept, separate from keeping it secure    |
| **Identity**                       | A verified statement of who a person, application or job is                                         |
| **Encryption**                     | Scrambling data so it is unreadable without the key, at rest and in transit                         |
| **Tokenization**                   | Replacing a sensitive value with a stand-in that maps back only through a protected lookup          |
| **Purpose Limitation**            | Using data only for the purposes for which it was collected                                        |
| **Legal Hold**                    | A requirement to preserve data that would otherwise be deleted, due to litigation or investigation |
| **Referential Integrity**         | Relationships between datasets are valid (no orphaned records, no dangling references)             |
| **Federated Governance**          | Central standards with domain-level accountability and execution                                   |

---

## Common Pitfalls

- **Governance as gatekeeping** — if governance only says "no," people will find workarounds; enable safe paths
- **Quality without business context** — generic checks ("all fields must be populated") create noise; tie rules to business purpose
- **Observability without action** — detecting anomalies is useless if no one responds; define escalation paths
- **Policy as documentation only** — written policies that aren't enforced are suggestions, not governance
- **Centralized bottleneck** — one team approving everything doesn't scale; federate with clear standards
- **Ignoring deletion complexity** — deleting from the source doesn't delete from downstream copies; plan propagation
- **Treating privacy and security as the same** — security protects systems; privacy governs appropriate use of personal information
- **Standing credentials** — a pipeline holding a permanent database password is a breach waiting to happen; prefer short-lived, workload-issued credentials
- **No certification levels** — not all data products need the same rigor; tier your governance by criticality

<!-- flows:start -->

## Worked Flows That Use This Stage

- [Secure data sharing with partners](../examples/secure-data-sharing.md) — replicated, contracted, shared outward with a partner.
- [Retention and audit](../examples/compliance-retention.md) — kept for years, provable, then deleted.
- [Finance reporting from an ERP and CRM](../examples/finance-reporting.md) — batch, ERP and CRM, published as a governed data product.

See [Worked Flows](../examples/README.md) for the full catalogue.

<!-- flows:end -->
