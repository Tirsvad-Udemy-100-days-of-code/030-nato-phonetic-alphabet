# MIL-001 Repository foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-003 | pending |

---

## Purpose

Decide whether the repository has the structure, configuration and automation that the converter can be built on: a Python 3.13 project with a local virtual environment, pytest, a Doxygen configuration, a CI workflow and a public presentation (description and topics).

## Deliverable

A repository containing `pyproject.toml`, a Python `.gitignore`, the `src/` package skeleton with `constants.py` and the NATO CSV data file, an empty but running `tests/` folder, a `Doxyfile`, a CI workflow, two ADRs, and a repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python >=3.13`, an empty `dependencies` list and pytest as a development extra | Present | Missing or a runtime dependency is listed |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` and the Doxygen output | `git check-ignore` confirms each | Any entry missing |
| 3 | A fresh `.venv` installs the project with `python -m pip install -e ".[dev]"` and `python -m pytest` runs | Exit code 0 | Install or run fails |
| 4 | `doxygen Doxyfile` builds | Exit code 0 | Build fails |
| 5 | The CI workflow runs the same pytest command and passes the framework's workflow checklist | Review `Go` | Review `No-Go` |
| 6 | The repository description and at least 5 topics are set on the host | API returns both | Missing |
| 7 | `.env` is not tracked and no token appears in any tracked file | `git ls-files` and a search show none | Any hit |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase; follows the accepted Business Case, Stakeholder Analysis and Project Plan |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O3, O4, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — inside the plan's window (2026-10-14 to 2026-10-17).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Record architecture decisions | Write ADR-0001 (read the NATO data with the standard library `csv` module instead of Pandas, so the project has no runtime dependencies for S03) and ADR-0002 (KPI, BMC, BPMN and RA are skipped for a project of this size). | No | |
| 2 | Configure the Python project | Add `pyproject.toml` (Python 3.13 or newer, no runtime dependencies, pytest as a development extra, pytest and package settings) and a Python `.gitignore` that also ignores `.env`, `.venv` and Doxygen output. | No | |
| 3 | Create the package skeleton | Start from the code of `026-nato-alphabet` (same layers, tooling and CI) and create `src/nato_phonetic_alphabet/` with `constants.py` (data file name, prompt and message texts), the supplied `nato_phonetic_alphabet.csv` as package data, and an empty `tests/` package, so the converter has a place to land. | No | |
| 4 | Add the Doxyfile | Generate a `Doxyfile` that reads `src/`, writes to `build/doxygen/`, extracts Python docstrings and warns on undocumented members. | No | |
| 5 | Add the CI workflow | Add a Gitea Actions workflow that sets up Python 3.13, creates a venv, installs the project and runs `python -m pytest` on every push and pull request. | No | |
| 6 | Set repository description and topics | Use the Gitea API with the token from the git-ignored `.env` (never printed, imported or committed) to set a description and topics on `Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet` so S03 sees what the repository is. | No | |

---

[BC-001]: ../business-case.md
