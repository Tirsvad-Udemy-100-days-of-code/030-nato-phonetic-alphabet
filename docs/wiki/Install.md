# Install

🌐 **English** · [Dansk](Install-da) · [Bahasa Melayu](Install-ms)

## What you need

- Python 3.13 or newer with the `venv` module
- Git

## Steps

Every system does the same four things: clone the repository, create a virtual environment called `.venv`, upgrade pip, install the project.

### Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet.git
cd 030-nato-phonetic-alphabet
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, run `Set-ExecutionPolicy -Scope Process RemoteSigned` first. It only applies to that window.

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

## Check that it works

```bash
python -m nato_phonetic_alphabet
```

Enter a word. You should see its code words. Next: [Usage](Usage).
