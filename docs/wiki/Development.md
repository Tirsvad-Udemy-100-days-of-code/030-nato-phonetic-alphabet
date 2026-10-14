# Development

🌐 **English** · [Dansk](Development-da) · [Bahasa Melayu](Development-ms)

Set up the project first ([Install](Install)). The `dev` extra installs pytest, ruff, mypy and import-linter.

## Run the tests

```bash
python -m pytest
```

## Run the checks that CI runs

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## Build the source documentation

```bash
doxygen Doxyfile
```

Open `build/html/index.html`. Install Doxygen from [doxygen.nl](https://www.doxygen.nl/) or your package manager.

## How the exception handling works

`spell_word` (in `domain/spelling.py`) looks every letter up in the dictionary inside a `try` block. A character that is not in the alphabet raises a `KeyError`, which the `except` block turns into an `InvalidWordError`. `generate_phonetic` (in `application/phonetic.py`) catches that error, tells the user to enter letters only and asks again until the word is valid.

## Code layout

| Folder | Content |
| --- | --- |
| `src/nato_phonetic_alphabet/domain/` | The spelling rule, with no input or output |
| `src/nato_phonetic_alphabet/application/` | The use case and its ports |
| `src/nato_phonetic_alphabet/adapters/` | The CSV reader and the console |
| `src/nato_phonetic_alphabet/constants.py` | Every literal of the program |
| `tests/` | pytest tests, mirroring `src/` |

Dependencies point inward: adapters know the application, the application knows the domain. import-linter enforces it.

## Pull requests

One branch and one pull request per milestone; CI must be green. The project follows the SQA and QC framework in `framework/`; see `docs/` for the plan and the review records.
