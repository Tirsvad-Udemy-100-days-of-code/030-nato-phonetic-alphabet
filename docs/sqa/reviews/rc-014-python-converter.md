# SQA Review Record RC-014: PY-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [PY-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Review of PY-002 | [80ec1bc] |

---

## Artifact Under Review

- Instance reviewed: [PY-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff rule set N passes; modules snake_case, classes PascalCase, `InvalidWordError` ends in Error; ruff rule set N passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose: `generate_phonetic`, `spell_word`, `load_nato_dict`, `TerminalConsole`. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff 0.17.0 check and format pass; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; mypy --strict passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `spell_word` catches the specific `KeyError` and raises `InvalidWordError` `from` it; `generate_phonetic` catches only `InvalidWordError`; the console adapter maps only EOFError and KeyboardInterrupt to `InputClosedError`; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; `path` defaults to None. |
| 7 | Files, locks and connections are managed with context managers | Pass | The CSV is read inside a `with` block. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class, function and constant has a Doxygen docstring; doxygen reports 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `print` and `input` are confined to `adapters/console.py` because the console is the program's output; there is no logging and no secret or personal data. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No design class diagram exists; MIL-002 plans none (the SSD and use case are the design artifacts). Classes follow the ports in `application/ports.py`. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 49 tests named for behaviour; `tmp_path` and fakes; no network; order independent. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict: no issues in 18 files; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; development tools pinned with `==`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each literal is defined once in `constants.py`; the letter mapping is defined once in the CSV. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | import-linter contract `Dependencies point inward` is kept; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `WordConsole` is a narrow Protocol; `generate_phonetic` depends on it and `TerminalConsole` implements it. |

## Overall Verdict

Go — every Mandatory criterion of QC-PY-001 passes or is not applicable (criterion 10: no design class diagram is planned). `generate_phonetic` takes the alphabet and the console as parameters because the application layer may not read files or call `input`; the assignment's name is kept. The `try`/`except KeyError` is in the domain function `spell_word` and the retry loop is in `generate_phonetic`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[PY-002]: ../../../src/nato_phonetic_alphabet/main.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[80ec1bc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/80ec1bc3640e1aa2ad1f152b9f71df39fa71c2d1
