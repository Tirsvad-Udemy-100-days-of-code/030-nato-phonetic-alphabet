# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-002 | [f42e610] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table and a conflict about the stand-in reviewer; set the domain to education; reviewed in autonomous mode, not independent | pending |

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

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Program converts words correctly, handles invalid input without crashing, and the structure follows the framework | Functionality, Supportability |
| CN-002 | S01 | Tests and CI give confidence | Reliability |
| CN-003 | S02 | Code is readable and keeps the assignment's function names | Supportability |
| CN-004 | S02 | The README tells how to create the `.venv` and run program and tests | Usability |
| CN-005 | S03 | Description, topics and README explain the repository at a glance | Usability |
| CN-006 | S03 | No runtime dependencies to install | Plus: implementation constraint |
| CN-007 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's location | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Pull request with review record and run summary | Every milestone |
| S02 | README and wiki | When the documentation milestone ships | Run instructions, screenshots, wiki in en, da, ms | MIL-003 |
| S03 | Repository page (description, topics, README) | Once | Description, topics, README | MIL-001, MIL-003 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-004] |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | [MIL-004] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 follows the lecture, which uses Pandas; S03 wants no runtime dependencies | S01, S03 | Use the standard library `csv` module; the dictionary comprehension is unchanged. Recorded in an architecture decision record (ADR) |
| The assignment's function names vs. the project's naming conventions | S02, S01 | Keep the assignment's function names in the public API; internal helpers follow the conventions |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct program with project structure (CN-001) | [BC-001] O1, O2 |
| S01 | Tests and CI (CN-002) | [BC-001] O3 |
| S02 | Readable code, run instructions (CN-003, CN-004) | [BC-001] O1, O2, O4 |
| S03 | Presentation and no dependencies (CN-005, CN-006) | [BC-001] O4, O5 |
| S01 | The project follows the common baseline of the framework (CN-007) | [BC-001] O6 |

## Sign-Off

Reviewer: S01 (in autonomous mode the AI acts as S01's stand-in; the review record states this).

The changes of the baseline milestone were accepted by the AI stand-in for S01 after the review record of this document (Go), autonomous, not independent.

---

[BC-001]: ./business-case.md
[f42e610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/f42e6109ac82937291e5c8207c0631f710b9da85
[MIL-004]: ./milestones/mil-004-framework-baseline.md
