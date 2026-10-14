# Usage

🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

Activate the virtual environment (see [Install](Install)), then start the program:

```bash
python -m nato_phonetic_alphabet
```

The installed command does the same:

```bash
nato-phonetic-alphabet
```

## Spell a word

The program asks for a word and prints the NATO code word of each letter, in order. Upper and lower case give the same result.

![The tool spelling the word Hello](images/spell-word.png)

## Invalid input

A digit, a space or a punctuation mark is not a letter. The program says so and asks again.

![A word with a digit is rejected, then a valid word is spelled](images/retry-invalid.png)

## Press Ctrl+C or Ctrl+D

Ending the input (Ctrl+D on Linux and macOS, Ctrl+Z then Enter on Windows) or pressing Ctrl+C closes the program quietly.
