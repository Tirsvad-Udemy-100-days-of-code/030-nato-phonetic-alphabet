# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, adapted from the 026 NATO alphabet project | [1da8981] |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Reviewed in RC-011 | pending |

---

## Purpose and Scope

The epic is [MIL-002] "NATO converter": the console behaviour that turns a typed word into NATO code words.

## Story List

### US-001.01 — Spell a word

**As a** User, **I want** to type a word and see the NATO code word of each of its letters, **so that** I can spell the word clearly over the phone.

**Acceptance Criteria**

- Given the program is running, when I enter `Hello`, then it lists `Hotel`, `Echo`, `Lima`, `Lima`, `Oscar` in that order.
- Given the program is running, when I enter the same word in lower case or upper case, then the result is the same.
- Given the program is running, when I enter a word with a character that is not a letter, then the program does not crash, tells me to enter only letters of the alphabet and asks for the word again.
- Given I entered an invalid word, when I then enter a valid word, then it lists the code words of that word.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [UC-001] | fits one iteration | none |

## INVEST Check

Independent (no other story is needed), Negotiable (wording of the messages is open), Valuable (it is the whole purpose of the tool), Estimable, Small (one console interaction) and Testable (each criterion is a pytest case). No exceptions.

---

[UCD-001]: ./use-case-diagram.md
[BC-001]: ./business-case.md
[MIL-002]: ./milestones/mil-002-nato-converter.md
[UC-001]: ./uc-001/uc.md
[1da8981]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/1da8981
