# Installation

🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install-ms)

## Det skal du bruge

- Python 3.13 eller nyere med modulet `venv`
- Git

## Trin

Alle systemer gør de samme fire ting: klon repository'et, opret et virtuelt miljø kaldet `.venv`, opgradér pip og installér projektet.

### Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet.git
cd 030-nato-phonetic-alphabet
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Hvis PowerShell afviser aktiveringsscriptet, så kør først `Set-ExecutionPolicy -Scope Process RemoteSigned`. Det gælder kun for det vindue.

### Linux Debian

```bash
sudo apt install git python3 python3-venv
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet.git
cd 030-nato-phonetic-alphabet
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### macOS

```bash
brew install python@3.13 git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet.git
cd 030-nato-phonetic-alphabet
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Tjek at det virker

```bash
python -m nato_phonetic_alphabet
```

Skriv et ord. Du skal se dets kodeord. Næste side: [Brug](Usage-da).
