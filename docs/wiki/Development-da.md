# Udvikling

🌐 [English](Development) · **Dansk** · [Bahasa Melayu](Development-ms)

Sæt projektet op først ([Installation](Install-da)). Udvidelsen `dev` installerer pytest, ruff, mypy og import-linter.

## Kør testene

```bash
python -m pytest
```

## Kør de kontroller, CI kører

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## Byg kildedokumentationen

```bash
doxygen Doxyfile
```

Åbn `build/html/index.html`. Installér Doxygen fra [doxygen.nl](https://www.doxygen.nl/) eller din pakkehåndtering.

## Sådan virker exception handling

`spell_word` (i `domain/spelling.py`) slår hvert bogstav op i ordbogen i en `try`-blok. Et tegn, der ikke findes i alfabetet, giver en `KeyError`, som `except`-blokken gør til en `InvalidWordError`. `generate_phonetic` (i `application/phonetic.py`) fanger fejlen, beder brugeren skrive kun bogstaver og spørger igen, indtil ordet er gyldigt.

## Kodens opbygning

| Mappe | Indhold |
| --- | --- |
| `src/nato_phonetic_alphabet/domain/` | Staveregelen, uden input og output |
| `src/nato_phonetic_alphabet/application/` | Use casen og dens porte |
| `src/nato_phonetic_alphabet/adapters/` | CSV-læseren og konsollen |
| `src/nato_phonetic_alphabet/constants.py` | Alle programmets konstanter |
| `tests/` | pytest-tests, som spejler `src/` |

Afhængigheder peger indad: adapters kender applikationen, applikationen kender domænet. import-linter håndhæver det.

## Pull requests

Én gren og én pull request pr. milepæl; CI skal være grøn. Projektet følger SQA- og QC-frameworket i `framework/`; se `docs/` for planen og review-optegnelserne.
