# ADR-0001 Read the NATO data with the standard library csv module

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-006 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lecture reads the NATO alphabet file into a Pandas DataFrame and builds the dictionary with `iterrows`. The file has 26 rows and two columns. S01 follows the lecture, but S03 wants a repository with no runtime dependencies, and [BC-001] objective O5 and constraint "no runtime dependencies unless needed" say the same.

Options evaluated:

1. Pandas, as in the lecture: matches the course, but adds a large runtime dependency for a 26-row table.
2. Polars: smaller than Pandas, still a runtime dependency that the task does not need.
3. The standard library `csv` module: no dependency, and the dictionary comprehension that the assignment teaches works unchanged on the rows of `csv.DictReader`.

## Decision

Read the NATO alphabet with the standard library `csv` module (`csv.DictReader`) and build the letter-to-code-word dictionary with a dictionary comprehension. The project declares no runtime dependencies.

## Consequences

**Positive:**

- No runtime dependency to install or keep secure; S03 sees an empty dependency list.
- Faster start and a smaller environment for S02.
- The comprehension taught in the lecture is still used.

**Negative:**

- The code differs from the lecture's Pandas code, so S02 comparing line by line sees a difference.
- A later day that needs Pandas has to add it explicitly.

## Affected Artifacts

- [BC-001] — meets objective O5 and the constraint on runtime dependencies.
- [SA-001] — resolves the conflict between S01 and S03 listed there.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
