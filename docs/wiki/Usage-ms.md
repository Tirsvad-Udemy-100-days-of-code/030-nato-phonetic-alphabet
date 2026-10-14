# Penggunaan

🌐 [English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

Aktifkan persekitaran maya (lihat [Pemasangan](Install-ms)), kemudian mulakan program:

```bash
python -m nato_phonetic_alphabet
```

Arahan yang dipasang melakukan perkara yang sama:

```bash
nato-phonetic-alphabet
```

## Eja satu perkataan

Program meminta satu perkataan dan mencetak kata kod NATO bagi setiap huruf mengikut urutan. Huruf besar dan huruf kecil memberi keputusan yang sama.

![Alat mengeja perkataan Hello](images/spell-word.png)

## Input tidak sah

Angka, ruang atau tanda baca bukan huruf. Program memberitahu perkara itu dan bertanya semula.

![Perkataan dengan angka ditolak, kemudian perkataan yang sah dieja](images/retry-invalid.png)

## Tekan Ctrl+C atau Ctrl+D

Menamatkan input (Ctrl+D di Linux dan macOS, Ctrl+Z kemudian Enter di Windows) atau menekan Ctrl+C menutup program dengan senyap.
