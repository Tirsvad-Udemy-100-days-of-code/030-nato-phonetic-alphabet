# UC-001 Spell a Word

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-012 | [80ec1bc] |

---

**Format:** Fully Dressed

## Fully Dressed

- **Scope:** NATO alphabet tool
- **Level:** user-goal
- **Primary Actor:** User, as named in [UCD-001]
- **Stakeholders and Interests:**
  - S01 — a correct result for every letter, kept simple
  - S02 — a readable behaviour that can be compared with their own solution
- **Preconditions:** the NATO alphabet data is available to the tool
- **Postconditions (success guarantee):** the User has seen the NATO code word of each letter of the word, in the order of the letters

### Main Success Scenario

1. The User starts the tool.
2. The tool asks for a word.
3. The User enters a word made of letters.
4. The tool shows the NATO code word of each letter, in order.

### Extensions (Alternative / Exception Flows)

- 3a. The word contains a character that is not a letter:
  1. The tool catches the failed lookup (exception handling), tells the User to enter only letters of the alphabet and does not crash.
  2. The tool asks for a word again (back to step 2).

### Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 3 | Upper-case and lower-case letters give the same result |
| 4 | Each letter A to Z maps to exactly one code word from the supplied alphabet |

### Open Issues

- None.

---

[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[SA-001]: ../stakeholder-analysis.md
[80ec1bc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/80ec1bc3640e1aa2ad1f152b9f71df39fa71c2d1
