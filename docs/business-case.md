# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-001 | [f42e610] |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective O6, success criterion 7, a scope item, a risk, an assumption and a constraint exception for the baseline milestone MIL-004; added the link definitions of the cited documents; set the domain to education; reviewed in autonomous mode, not independent | [7378ede] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Scope wording: the baseline milestone includes one behaviour-neutral rewrite of the imports of `csv_alphabet.py` so the OpenGrep scan passes; reviewed in autonomous mode, not independent | [90fbd21] |

---

## Executive Summary

Day 30 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" extends the NATO phonetic alphabet console tool with exception handling: the user types a word and the program spells it out, and when the input holds a character that is not a letter the program catches the failed lookup, tells the user to enter letters only and asks again instead of crashing. This project delivers that assignment as a clean, tested, documented Python repository that other course participants and GitHub visitors can read, run and compare against their own solutions. It uses only the Python standard library at runtime. A later milestone, [MIL-004], brings the finished project to the baseline of the framework.

## Methodological and Standards Foundation

- Methodology: the project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, one pull request per milestone).
- Quality model: ISO/IEC 25010:2023 characteristics tag every QC criterion; code is reviewed against `qc-programming-python.md`.
- Engineering practice: Clean Architecture layering at a size proportionate to the program, tests written with pytest, source documented with Doxygen comments.

## Problem Statement

- The course assignment ships as a loose `main.py` and a CSV file with no tests, no run instructions and no project structure, so a participant cannot easily share or compare a solution.
- Without exception handling the program crashes with a `KeyError` as soon as the user types a digit or a symbol.
- Public solutions to course assignments are often undocumented, depend on heavy libraries (the course uses Pandas for a 26-row table) and are not runnable without guesswork.

## Business Opportunity

A small, exemplary solution lets the Product Owner practise professional project hygiene (packaging, tests, CI, documentation, multilingual wiki) on a trivially small domain, and gives other learners and GitHub visitors a reference they can run in a minute.

## Objectives

1. O1: Deliver a console program that converts a word typed by the user into the list of NATO phonetic code words, built with list and dictionary comprehensions, that handles invalid input with `try`/`except` and asks again until the input is valid, keeping the assignment's function names (`generate_phonetic`).
2. O2: Make the repository runnable by following the README on Windows PowerShell, Debian Linux and macOS with a local `.venv`.
3. O3: Cover the behaviour with automated pytest tests that run in continuous integration.
4. O4: Document the source with Doxygen comments and a `Doxyfile`, and document the project in a README and a wiki in English, Danish and Bahasa Malaysia, with screenshots.
5. O5: Present the repository to GitHub viewers with a description and topics, and with no runtime dependencies.
6. O6: Bring the finished project to the common baseline of the framework: the adopted framework release, the wiki in the framework's location `docs/wiki/`, complete licence metadata and review records for every changed document ([MIL-004]).

## Scope

### In Scope

- Console program: reads a word, prints the NATO code words for its letters; catches the error and asks again when the input contains a character that is not a letter.
- NATO alphabet data file (comma-separated values, CSV, as supplied with the assignment) and a loader that uses the standard library.
- Project structure `src/`, `tests/`, `docs/`; `pyproject.toml`; `constants.py`; Python `.gitignore`; `Doxyfile`.
- pytest test suite; continuous integration (CI) workflow that runs the tests.
- README from the framework template; wiki pages in en, da and ms; screenshots for README and wiki.
- Repository description and topics on the git host.
- The baseline milestone [MIL-004]: framework release, wiki completed in `docs/wiki/`, README appendix, licence metadata, review records and the traceability matrix. It changes no behaviour of the program; its only change in `src/` is the rewrite of the imports of one adapter module so the OpenGrep scan passes (task 6).

### Out of Scope

- A graphical or web interface.
- Publishing a package to the Python Package Index (PyPI).
- Runtime dependencies such as Pandas.
- Non-Latin alphabets and digits (rejected with a message).
- Other course days.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-004], except the behaviour-neutral rewrite of the imports of `src/nato_phonetic_alphabet/adapters/csv_alphabet.py` (task 6).

## Expected Benefits

### Tangible Benefits

- A runnable, tested reference solution with a one-command test run.
- A reusable repository skeleton (pyproject, continuous integration, Doxygen, wiki) for later course days.

### Intangible Benefits

- Practice in professional project hygiene.
- A readable example for other learners, in three languages.

## Strategic Alignment

The project supports the Product Owner's personal goal of completing the 100 Days of Code bootcamp with portfolio-quality repositories, and the framework's goal of demonstrating the plan-first workflow on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Program spells a word correctly | Every letter A-Z maps to its NATO code word; input is case-insensitive | pytest: all 26 letters and a mixed-case word pass |
| 1a | Invalid input is handled | A character that is not a letter never crashes the program; the user is told and asked again | pytest: a digit and a symbol are rejected and a later valid word is spelled |
| 2 | Tests pass | 100 % of tests pass on Python 3.13 locally and in CI | `python -m pytest` exit code 0; CI run green |
| 3 | No runtime dependencies | 0 runtime dependencies | `pyproject.toml` has an empty `dependencies` list |
| 4 | Setup works from the README | A fresh clone runs the program using only the README steps | Manual run of the README steps on Windows PowerShell |
| 5 | Documentation complete | README sections of the template, wiki in 3 languages, Doxygen builds without warnings | `check-readme.sh` exit 0; every wiki page exists in en, da and ms; `doxygen Doxyfile` reports 0 warnings |
| 6 | Repository presented | Description and at least 5 topics set | Repository page and API show both |
| 7 | The baseline milestone is done (O6) | Wiki pages in 3 languages in `docs/wiki/`, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the CI checks of the pull request of [MIL-004] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The git host token lacks scope for editing the repository or wiki | Description, topics or wiki cannot be published | Stop and report; keep the wiki content as files in the working tree and ask S01 for a token with the needed scope |
| The wiki is not enabled on the host | Wiki pages cannot be pushed | Enable it through the repository settings API; otherwise stop and report |
| Danish and Bahasa Malaysia translations contain errors | S02 or S03 read wrong text | Keep wiki sentences short and simple; S01 reviews the translations in the pull request |
| Starter code is copied verbatim | Originality concerns | The program is written fresh; only the supplied CSV data is reused, as the assignment intends |
| Secrets in `.env` leak into the repository | Credential exposure | `.env` is git-ignored, never imported by the program or tests, and never echoed |
| The documents of the baseline milestone [MIL-004] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- The Product Owner is S01, who also develops and reviews; in autonomous mode the AI acts as S01's stand-in reviewer and the review records say so.
- Python 3.13 or newer is available on the machines of the readers.
- The git host (Gitea) offers repository, topic and wiki features through its application programming interface (API) and git remote.
- The CSV with 26 letter/code word rows supplied with the assignment is the data source.
- The baseline milestone [MIL-004] is finished within one week of its own start, 2026-11-16, by 2026-11-23. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Constraints

- Python 3.13 or newer, a local `venv`, `pytest`, constants in `constants.py`, configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Tokens are read from `.env` for personal use only; the project and its tests never import or test it.
- One pull request per milestone; no commit on `main`.
- The baseline milestone [MIL-004] is the exception to the rule of one reviewer: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

## Cost–Benefit Assessment

Qualitative, because the project is a personal learning exercise with no revenue; the effort is a few hours of S01's time and AI assistance.

| Costs | Benefits |
| --- | --- |
| A few hours of effort; hosting on an existing git host | A reusable reference repository, practice with the framework, a shareable example for S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns and builds the project; wants a clean, complete solution |
| S02 | Wants readable, runnable code with the assignment's function names and run instructions |
| S03 | Wants a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed: the scope is small, the risks are low and every objective is verifiable.

---

[SA-001]: ./stakeholder-analysis.md
[f42e610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/f42e6109ac82937291e5c8207c0631f710b9da85
[PP-001]: ./project-plan.md
[MIL-004]: ./milestones/mil-004-framework-baseline.md
[7378ede]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/7378eded894a69048cfc5c5c56c787efc4723a4e
[90fbd21]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/90fbd2170d2f9295ad60edad82ef08ef96574ff6
