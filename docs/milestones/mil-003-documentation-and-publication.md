# MIL-003 Documentation and publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, adapted from the 026 NATO alphabet project | [80ec1bc] |

---

## Purpose

Decide whether S02 and S03 can understand, set up and run the project from its README and wiki without help, in English, Danish and Bahasa Malaysia.

## Deliverable

The `README.md` built from the framework template with screenshots, and a wiki in English, Danish and Bahasa Malaysia with the same pages and screenshots, published on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `check-readme.sh` reports no finding for the README | Exit code 0 | Any finding |
| 2 | The README steps (create `.venv`, upgrade pip, install, run, test) work on a fresh clone on Windows PowerShell | The run produces the expected output | A step fails |
| 3 | Every wiki page exists in en, da and ms | `check-languages.sh` and a file listing agree | A page is missing |
| 4 | The README and each wiki language show a screenshot | Image files exist and are linked | Missing |
| 5 | The wiki is published and readable on the host | Page requests return success | Any page not found |
| 6 | `doxygen Doxyfile` builds and the README says how | Exit code 0 and the section exists | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The documentation describes the finished program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O4, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — the end of the plan's window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots | Run the program and render its real output as PNG images (a word spelled, an invalid input retried) stored under `docs/images/` for the README and the wiki. | No | |
| 2 | Write the README | Fill the framework README template: set-up on Windows PowerShell, Linux Debian and macOS with a local `.venv` and `python -m pip install --upgrade pip`, run, tests, continuous integration, Doxygen build, layout and licence. | No | |
| 3 | Write the English wiki | Pages Home, Install, Usage and Development in English with screenshots, in the layout of the framework wiki. | No | |
| 4 | Write the Danish wiki | The same pages in Danish with the `-da` suffix. | No | |
| 5 | Write the Bahasa Malaysia wiki | The same pages in Bahasa Malaysia with the `-ms` suffix. | No | |
| 6 | Publish the wiki | Push the pages to the repository's wiki on the git host and check that each page is readable. | No | |
| 7 | Verify the set-up instructions | Follow the README from a fresh clone in a new `.venv`, run the program and the tests, and record the result in the review. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-nato-converter.md
[80ec1bc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/80ec1bc3640e1aa2ad1f152b9f71df39fa71c2d1
