# Pembangunan

🌐 [English](Development) · [Dansk](Development-da) · **Bahasa Melayu**

Sediakan projek dahulu ([Pemasangan](Install-ms)). Pilihan tambahan `dev` memasang pytest, ruff, mypy dan import-linter.

## Jalankan ujian

```bash
python -m pytest
```

## Jalankan semakan yang dijalankan oleh CI

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## Bina dokumentasi sumber

```bash
doxygen Doxyfile
```

Buka `build/html/index.html`. Pasang Doxygen dari [doxygen.nl](https://www.doxygen.nl/) atau pengurus pakej anda.

## Cara pengendalian pengecualian berfungsi

`spell_word` (dalam `domain/spelling.py`) mencari setiap huruf dalam kamus di dalam blok `try`. Aksara yang tiada dalam abjad menimbulkan `KeyError`, yang ditukar oleh blok `except` kepada `InvalidWordError`. `generate_phonetic` (dalam `application/phonetic.py`) menangkap ralat itu, meminta pengguna memasukkan huruf sahaja dan bertanya semula sehingga perkataan itu sah.

## Susun atur kod

| Folder | Kandungan |
| --- | --- |
| `src/nato_phonetic_alphabet/domain/` | Peraturan ejaan, tanpa input dan output |
| `src/nato_phonetic_alphabet/application/` | Kes guna dan portnya |
| `src/nato_phonetic_alphabet/adapters/` | Pembaca CSV dan konsol |
| `src/nato_phonetic_alphabet/constants.py` | Semua pemalar program |
| `tests/` | Ujian pytest, mencerminkan `src/` |

Kebergantungan menghala ke dalam: adapter mengenali aplikasi, aplikasi mengenali domain. import-linter menguatkuasakannya.

## Pull request

Satu cabang dan satu pull request bagi setiap milestone; CI mesti hijau. Projek ini mengikut rangka kerja SQA dan QC dalam `framework/`; lihat `docs/` untuk pelan dan rekod semakan.
