# MIL-002 NATO converter

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-004 | pending |

---

## Purpose

Decide whether the console program does what the Day 30 assignment asks: read a word, print the NATO code word of each letter, and handle invalid input with exception handling (a `try`/`except` on the failed dictionary lookup) inside `generate_phonetic`, which keeps asking until the input is valid. Tested with pytest.

## Deliverable

The `nato_phonetic_alphabet` package with a runnable entry point, a test suite that passes, and Doxygen comments on every public item; plus the user story, use case and system sequence diagram of "spell a word".

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | All 26 letters map to their code word and input is case-insensitive | pytest passes | Any test fails |
| 2 | A character that is not a letter raises a caught `KeyError`; the program tells the user to enter letters of the alphabet only and asks again instead of crashing | pytest covers it and passes | Missing or failing |
| 3 | The loader uses a dictionary comprehension, the converter a list comprehension, and the invalid input is handled with `try`/`except`, not with a pre-check | Code review confirms | Loops or pre-checks used instead |
| 4 | The assignment's function names are kept in the public API | Names present in the module | Names missing |
| 5 | The code review against `qc-programming-python.md` is a `Go` | `RC-*` verdict `Go` | `No-Go` |
| 6 | `doxygen Doxyfile` reports no warnings | 0 warnings | Any warning |
| 7 | Constants live in `constants.py`; `.env` is not imported by `src/` or `tests/` | Search confirms | Any hit |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Project configuration, skeleton, CI and Doxyfile |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O4 | [BC-001] |
| Spell a word | US-001, UC-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — inside the plan's window (2026-10-14 to 2026-10-16).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Model "spell a word" | Write US-001, UC-001 (brief) and the system sequence diagram for the user who types a word and receives its NATO code words, including the retry on invalid input. Domain concepts are only letter and code word, so no domain model is added. | Yes | US-001, UC-001 |
| 2 | Load the NATO alphabet | Read the CSV with the standard library and build the letter-to-code-word dictionary with a dictionary comprehension (`load_nato_dict`), taking the file name from `constants.py`. | No | |
| 3 | Convert a word to code words | Implement the assignment's `generate_phonetic`: it prompts for a word, builds the code words with a list comprehension inside a `try` block, catches the `KeyError` of a character that is not a letter, tells the user to enter letters of the alphabet only, and loops until the input is valid. The lookup and the prompt sit behind ports so the layers stay separate. | Yes | UC-001 |
| 4 | Implement the console entry point | Prompt for a word, print the code words, ask again on invalid input; runnable as `python -m nato_phonetic_alphabet` and as the `nato-phonetic-alphabet` command. | Yes | UC-001 |
| 5 | Write the pytest suite | Test all letters, mixed case, unknown characters, the loader (with a temporary CSV) and the entry point (with patched input and captured output). | No | |
| 6 | Add Doxygen comments | Document every module, function and constant with Doxygen comments and confirm the build has no warnings. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-repository-foundation.md
