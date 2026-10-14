# Pemasangan

🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

## Apa yang diperlukan

- Python 3.13 atau lebih baharu dengan modul `venv`
- Git

## Langkah

Semua sistem melakukan empat perkara yang sama: klon repositori, cipta persekitaran maya bernama `.venv`, naik taraf pip dan pasang projek.

### Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet.git
cd 030-nato-phonetic-alphabet
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jika PowerShell enggan menjalankan skrip pengaktifan, jalankan `Set-ExecutionPolicy -Scope Process RemoteSigned` dahulu. Ia hanya terpakai pada tetingkap itu.

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

## Semak ia berfungsi

```bash
python -m nato_phonetic_alphabet
```

Masukkan satu perkataan. Anda akan melihat kata kodnya. Seterusnya: [Penggunaan](Usage-ms).
