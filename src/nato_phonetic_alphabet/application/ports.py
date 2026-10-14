"""@brief Ports the use case needs from the outside world."""

from typing import Protocol


class InputClosedError(Exception):
    """@brief Raised when the user can give no more input (end of input, abort)."""


class WordConsole(Protocol):
    """@brief Port for the conversation with the user."""

    def ask_word(self) -> str:
        """@brief Ask the user for a word.

        @return The word as typed.
        @throws InputClosedError The user can give no more input.
        """
        ...

    def show_invalid(self) -> None:
        """@brief Tell the user that the word was rejected."""
        ...

    def show_code_words(self, code_words: list[str]) -> None:
        """@brief Show the result to the user.

        @param code_words The code words to show.
        """
        ...
