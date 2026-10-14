# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-002 | pending |

---

## Purpose

Identify who has a stake in the NATO alphabet project, how much power and interest each has, and what each needs from the repository. The analysis uses the power/interest grid and maps concerns to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad (personal) | HIGH | HIGH | Manage Closely | A correct, complete and well-structured solution that is easy to maintain |
| S02 | Udemy coursists | Fellow course participants who share and compare solutions | Udemy 100 Days of Code community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors browsing the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact, and is the only person who talks to the other stakeholders.
- **Keep Informed (S02, S03):** they cannot change the project but are its intended readers; their needs are met through the README, the wiki and the code itself. S02 has high interest because the repository is aimed at them; S03 is a passer-by with medium interest.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Program converts words correctly, handles invalid input without crashing, and the structure follows the framework | Functionality, Supportability |
| S01 | Tests and CI give confidence | Reliability |
| S02 | Code is readable and keeps the assignment's function names | Supportability |
| S02 | The README tells how to create the `.venv` and run program and tests | Usability |
| S03 | Description, topics and README explain the repository at a glance | Usability |
| S03 | No runtime dependencies to install | Plus: implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Pull request with review record and run summary | Every milestone |
| S02 | README and wiki | When the documentation milestone ships | Run instructions, screenshots, wiki in en, da, ms | MIL-003 |
| S03 | Repository page (description, topics, README) | Once | Description, topics, README | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 follows the lecture, which uses Pandas; S03 wants no runtime dependencies | S01, S03 | Use the standard library `csv` module; the dictionary comprehension is unchanged. Recorded in an architecture decision record (ADR) |
| The assignment's function names vs. the project's naming conventions | S02, S01 | Keep the assignment's function names in the public API; internal helpers follow the conventions |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct program with project structure | [BC-001] O1, O2 |
| S01 | Tests and CI | [BC-001] O3 |
| S02 | Readable code, run instructions | [BC-001] O1, O2, O4 |
| S03 | Presentation and no dependencies | [BC-001] O4, O5 |

## Sign-Off

Reviewer: S01 (in autonomous mode the AI acts as S01's stand-in; the review record states this).

---

[BC-001]: ./business-case.md
