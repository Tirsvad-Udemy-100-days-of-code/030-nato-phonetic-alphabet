# ADR-0002 Skip the optional analysis artifacts

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-007 | [f42e610] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The journey of the framework offers analysis documents beyond the baseline: KPI definitions, a Business Model Canvas, a BPMN process model and a riskiest-assumption test. The project is a single-evening course exercise with six measurable success criteria already in [BC-001], no commercial model, no business process and no costly belief to test.

Options evaluated:

1. Write all four documents: complete, but each needs a review and adds no decision that the Business Case does not already hold.
2. Write only the KPI definitions: the success criteria would be restated in another file.
3. Skip all four and record the reason here.

## Decision

Skip the KPI definitions, the Business Model Canvas, the BPMN process model and the riskiest-assumption test. The Business Case's Success Criteria table carries the measures, and the baseline documents (Business Case, Stakeholder Analysis, Project Plan, milestones) are not skipped.

## Consequences

**Positive:**

- Less documentation to keep consistent for a small project.
- The success criteria are stated once, in one place.

**Negative:**

- A reader who expects a KPI document finds the measures in the Business Case instead.
- If the project grows (a package published, more users), the skipped documents must be written then.

## Affected Artifacts

- [BC-001] — its Success Criteria stay the only definition of the measures.

---

[BC-001]: ../business-case.md
[f42e610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/f42e6109ac82937291e5c8207c0631f710b9da85
