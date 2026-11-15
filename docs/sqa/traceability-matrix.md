# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, rows for RC-001 to RC-014 | [b69a604] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline milestone, the wiki row, the new review records, the concern coverage and the domain education; reviewed in autonomous mode, not independent | [7378ede] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the cross-artifact traceability can be checked. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-015] (Go, re-review of the whole document), [RC-001] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-016] (Go, re-review of the whole document), [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-017] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone | en | education | [BC-001], [PP-001] | [MIL-002], [ADR-0001], [ADR-0002] | [RC-018] (Go, re-review after the metadata change), [RC-003] |
| [MIL-002] | Milestone | en | education | [BC-001], [MIL-001] | [MIL-003], [US-001], [UC-001], [PY-002] | [RC-019] (Go, re-review after the metadata change), [RC-004] |
| [MIL-003] | Milestone | en | education | [BC-001], [MIL-002] | [MIL-004] | [RC-020] (Go, re-review after the metadata change), [RC-005] |
| [MIL-004] | Milestone | en | education | [BC-001], [PP-001], [MIL-003] | - | [RC-021] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-004] | - | [RC-022] (Go-with-conditions) |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | [PY-001] | [RC-006] |
| [ADR-0002] | ADR | - | - | [BC-001] | - | [RC-007] |
| [WF-001] | CI workflow | - | - | [MIL-001] | - | [RC-008] |
| [UCD-001] | Use Case Diagram | en | education | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-010] |
| [US-001] | User Story | en | education | [UCD-001], [MIL-002] | [UC-001] | [RC-011] |
| [UC-001] | Use Case | en | education | [UCD-001], [US-001] | [SSD-001], [PY-002] | [RC-012] |
| [SSD-001] | System Sequence Diagram | en | education | [UC-001] | [PY-002] | [RC-013] |
| [PY-002] | Python source | - | - | [UC-001], [SSD-001], [ADR-0001] | - | [RC-014] |
| [PY-001] | Python source | - | - | [ADR-0001], [MIL-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-002] | - | - | Covered |
| CN-003 | [MIL-002] | - | - | Covered |
| CN-004 | [MIL-003] | - | - | Covered |
| CN-005 | [MIL-001], [MIL-003] | - | - | Covered |
| CN-006 | [MIL-001] | [ADR-0001] | - | Covered |
| CN-007 | [MIL-004] | - | - | Covered |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no review record exists.
- PP-001 was accepted by the Product Owner's stand-in without a review record; [RC-017] is its first review, against QC-PP-001.
- WF-001 and PY-001 are labels for reviewed code instances (no artifact file).
- PY-002 is the label of the reviewed converter code.
- The domain of every artifact is `education` since [MIL-004]; the earlier review records state the former domain `it` as it was at the time.
- The source code and the workflow are reviewed in the records RC-008, RC-009 and RC-014 and not again in [MIL-004], which changes no source file.
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-repository-foundation.md
[MIL-002]: ../milestones/mil-002-nato-converter.md
[MIL-003]: ../milestones/mil-003-documentation-and-publication.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[SA-001]: ../stakeholder-analysis.md
[ADR-0001]: ../adr/adr-0001-read-nato-data-with-csv-module.md
[ADR-0002]: ../adr/adr-0002-skip-analysis-artifacts.md
[WF-001]: ../../.gitea/workflows/ci.yml
[PY-001]: ../../src/nato_phonetic_alphabet/constants.py
[RC-006]: ./reviews/rc-006-adr-0001.md
[RC-007]: ./reviews/rc-007-adr-0002.md
[RC-008]: ./reviews/rc-008-ci-workflow.md
[RC-009]: ./reviews/rc-009-python-skeleton.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[PY-002]: ../../src/nato_phonetic_alphabet/main.py
[RC-010]: ./reviews/rc-010-ucd-001.md
[RC-011]: ./reviews/rc-011-us-001.md
[RC-012]: ./reviews/rc-012-uc-001.md
[RC-013]: ./reviews/rc-013-ssd-001.md
[RC-014]: ./reviews/rc-014-python-converter.md
[b69a604]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/b69a604341251be410672cee93910e528eecaef8
[MIL-004]: ../milestones/mil-004-framework-baseline.md
[RC-015]: ./reviews/rc-015-business-case-baseline.md
[RC-016]: ./reviews/rc-016-stakeholder-analysis-baseline.md
[RC-017]: ./reviews/rc-017-project-plan-baseline.md
[RC-018]: ./reviews/rc-018-milestone-001-baseline.md
[RC-019]: ./reviews/rc-019-milestone-002-baseline.md
[RC-020]: ./reviews/rc-020-milestone-003-baseline.md
[RC-021]: ./reviews/rc-021-milestone-004.md
[RC-022]: ./reviews/rc-022-wiki.md
[7378ede]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/7378eded894a69048cfc5c5c56c787efc4723a4e
