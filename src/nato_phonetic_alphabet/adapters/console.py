"""@brief Adapter that talks to the user through the terminal."""

from nato_phonetic_alphabet import constants
from nato_phonetic_alphabet.application.ports import InputClosedError


class TerminalConsole:
    """@brief WordConsole port implemented on standard input and output."""

    def ask_word(self) -> str:
        """@brief Prompt for a word.

        @return The word as typed.
        @throws InputClosedError Input ended or the user interrupted it.
        """
        try:
            return input(constants.PROMPT_TEXT)
        except (EOFError, KeyboardInterrupt) as error:
            raise InputClosedError from error

    def show_invalid(self) -> None:
        """@brief Print that the word was rejected."""
        print(constants.INVALID_INPUT_TEXT)

    def show_code_words(self, code_words: list[str]) -> None:
        """@brief Print the result.

        @param code_words The code words to print.
        """
        print(constants.RESULT_TEXT)
        print(*code_words, sep="\n")
