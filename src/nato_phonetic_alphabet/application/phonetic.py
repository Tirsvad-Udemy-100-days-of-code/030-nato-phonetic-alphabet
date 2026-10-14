"""@brief Use case: ask for a word until it can be spelled."""

from collections.abc import Mapping

from nato_phonetic_alphabet.application.ports import WordConsole
from nato_phonetic_alphabet.domain.spelling import InvalidWordError, spell_word


def generate_phonetic(alphabet: Mapping[str, str], console: WordConsole) -> list[str]:
    """@brief Ask for a word until it is valid, then return its code words.

    This is the assignment's `generate_phonetic`: it wraps the input and the
    error handling. An invalid word is reported to the user and asked for
    again, so the function returns only for a valid word.

    @param alphabet Code word per upper-case letter.
    @param console Conversation with the user.
    @return The code words of the word the user typed.
    @throws InputClosedError The user can give no more input.
    """
    while True:
        word = console.ask_word()
        try:
            return spell_word(word, alphabet)
        except InvalidWordError:
            console.show_invalid()
