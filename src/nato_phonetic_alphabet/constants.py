"""@brief Constants of the NATO alphabet tool.

Every literal that the program, its messages or its data loading depend on is
defined here once.
"""

## @brief Name of the package that holds the data file.
DATA_PACKAGE: str = "nato_phonetic_alphabet"

## @brief Folder inside the package that holds the data file.
DATA_DIRECTORY: str = "data"

## @brief Name of the comma-separated values file with the NATO alphabet.
DATA_FILE_NAME: str = "nato_phonetic_alphabet.csv"

## @brief Header of the column with the letter in the data file.
LETTER_COLUMN: str = "letter"

## @brief Header of the column with the code word in the data file.
CODE_COLUMN: str = "code"

## @brief Text shown when the program asks for a word.
PROMPT_TEXT: str = "Enter a word: "

## @brief Text shown when the word holds a character that is not a letter.
INVALID_INPUT_TEXT: str = "Sorry, only the letters A to Z are allowed. Try again."

## @brief Text shown before the code words are printed.
RESULT_TEXT: str = "Phonetic code words:"

## @brief Text encoding of the data file.
DATA_ENCODING: str = "utf-8"

## @brief Exit status of a session that ended normally.
EXIT_OK: int = 0
