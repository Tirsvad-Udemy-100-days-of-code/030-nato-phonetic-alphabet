# Project Plan

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted as Product Owner stand-in (no QC checklist for PP yet); plan accepted by S01 in chat | [f42e610] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline gateway MIL-004, its schedule row, scope coverage, dependency, risk and Gantt entries, the No-Go rule and an open issue; linked the git host milestones of MIL-001 to MIL-003; set the domain to education; reviewed in autonomous mode, not independent | [7378ede] |

---

## Purpose

Schedule the three phases that deliver the Day 30 NATO alphabet assignment as a tested and documented repository: foundation, converter, documentation and publication. The plan runs against the Business Case's constraint of a small personal project with one pull request per milestone. A fourth gateway, [MIL-004], was added on 2026-11-16 to bring the finished project to the baseline of the framework; it runs from 2026-11-16 to 2026-11-23.

## Planning Assumptions

- The plan starts 2026-10-14; its first three gateways end by 2026-10-16 and the baseline gateway [MIL-004] ends by 2026-11-23.
- Each phase is one day of work and one pull request that closes its issues.
- S01 is owner and reviewer of every gateway; in autonomous mode the AI acts as S01's stand-in and every review record says so.
- The baseline gateway [MIL-004] starts 2026-11-16 and ends by 2026-11-23, one week (source: [BC-001], Assumptions). It is the only gateway outside the one-day windows of the first three, because of the agreed minimum quality baseline of the framework.
- For [MIL-004] S01 has authorised the assistant to commit, push, open the pull request and merge it, and the review is done by an AI stand-in for S01 (source: [BC-001], Constraints; [SA-001], Conflicting Interests and Mitigations).
- The language of the planning documents is English (registry `Languages`); the wiki is written in English, Danish and Bahasa Malaysia.
- The git host is the Gitea instance at `git.tirsystem.com`; its token comes from the git-ignored `.env`.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Repository foundation | [MIL-001] | 2026-10-14 to 2026-10-14 | 2026-10-14 | S01 | none | Project configuration, package skeleton, Doxyfile, CI workflow, ADRs, repository description and topics | [Milestone 159][MS-159] |
| NATO converter | [MIL-002] | 2026-10-14 to 2026-10-15 | 2026-10-15 | S01 | US-001 | Working console program with pytest tests and Doxygen comments | [Milestone 160][MS-160] |
| Documentation and publication | [MIL-003] | 2026-10-15 to 2026-10-16 | 2026-10-16 | S01 | none | README, screenshots, wiki in en, da and ms | [Milestone 161][MS-161] |
| Framework baseline | [MIL-004] | 2026-11-16 to 2026-11-23 | 2026-11-23 | S01 | none | The framework release, the wiki in `docs/wiki/`, the licence metadata, the traceability matrix and the review records | [Milestone 542][MS-542] |

```plantuml
@startgantt
Project starts 2026-10-14
[Repository foundation] starts 2026-10-14 and ends 2026-10-14
[MIL-001 Go/No-Go] happens 2026-10-14
[NATO converter] starts 2026-10-14 and ends 2026-10-15
[MIL-002 Go/No-Go] happens 2026-10-15
[Documentation and publication] starts 2026-10-15 and ends 2026-10-16
[Framework baseline] starts 2026-11-16 and ends 2026-11-23
[MIL-003 Go/No-Go] happens 2026-10-16
[Framework baseline Go/No-Go] happens 2026-11-23
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Console program and NATO data loader | [MIL-002] |
| Project structure, `pyproject.toml`, `constants.py`, `.gitignore`, `Doxyfile` | [MIL-001] |
| pytest test suite | [MIL-002] |
| CI workflow that runs the tests | [MIL-001] |
| README, wiki (en, da, ms) and screenshots | [MIL-003] |
| Repository description and topics | [MIL-001] |
| The baseline: framework release, wiki location, licence metadata, traceability matrix, review records | [MIL-004] |

## Dependencies

```
MIL-001 → MIL-002 → MIL-003 → MIL-004
```

A No-Go on a gateway holds the later ones until the cause is fixed and the gateway is reviewed again; later windows shift by the same days. A No-Go on [MIL-004] leaves the program and the earlier gateways as they are; S01 decides the new date.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The host token lacks scope for repository settings or wiki | MIL-001 or MIL-003 cannot finish | Stop and report (autonomous-mode stop rule); S01 supplies a token with the scope |
| The CI runner on the host is not available | CI workflow cannot be proven green | The workflow is verified by running the same commands locally; the gap is recorded in the review |
| Wiki translation takes longer than planned | MIL-003 slips | Wiki pages are short and share one structure |
| A continuous integration (CI) check fails on the pull request of [MIL-004] | The merge is delayed past 2026-11-23 | The failure is fixed on the same branch and the checks run again; after three failed rounds on one cause the work stops and S01 decides (trace: success criterion 7 of [BC-001]) |

## Open Issues

- "Python greater than 3.13" is read as 3.13 or newer (`requires-python = ">=3.13"`); S01 can tighten it.
- `.env` also holds a GitHub token and user; no GitHub mirror was requested, so they are not used.
- Screenshots are rendered from the real program output (a terminal-style image), because a desktop screenshot cannot be taken from an unattended run; S01 may replace them with native captures.
- Framework baseline (closed in [MIL-004]): the wiki pages, which already were in `docs/wiki/`, the location the framework requires, got the language line first, the screenshots from the repository and the Project-Documents page; [MIL-003] (deliverable and criterion 3) still says only that the wiki is published, as it was accepted. Every document with a `Domain` row now has the domain `education`.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-repository-foundation.md
[MIL-002]: ./milestones/mil-002-nato-converter.md
[MIL-003]: ./milestones/mil-003-documentation-and-publication.md
[f42e610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/f42e6109ac82937291e5c8207c0631f710b9da85
[MIL-004]: ./milestones/mil-004-framework-baseline.md
[MS-159]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/milestone/159
[MS-160]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/milestone/160
[MS-161]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/milestone/161
[MS-542]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/milestone/542
[7378ede]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/7378eded894a69048cfc5c5c56c787efc4723a4e
