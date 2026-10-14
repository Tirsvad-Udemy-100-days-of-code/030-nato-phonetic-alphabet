"""@brief Rule that spells a word with the NATO phonetic alphabet."""

from collections.abc import Mapping


class InvalidWordError(ValueError):
    """@brief Raised when a word cannot be spelled.

    A word is invalid when it is empty or holds a character that is not a
    letter A to Z.
    """


def spell_word(word: str, alphabet: Mapping[str, str]) -> list[str]:
    """@brief Spell a word with the code word of each of its letters.

    The list comprehension looks every letter up in the alphabet. A character
    that is not in the alphabet makes the lookup fail with a `KeyError`, which
    is caught here and turned into an `InvalidWordError`. The match is
    case-insensitive.

    @param word The word to spell.
    @param alphabet Code word per upper-case letter.
    @return The code words, one per letter of the word, in order.
    @throws InvalidWordError The word is empty or holds a character that is
        not a letter of the alphabet.
    """
    if not word:
        raise InvalidWordError("The word is empty.")
    try:
        return [alphabet[letter.upper()] for letter in word]
    except KeyError as error:
        raise InvalidWordError(f"Not a letter: {error.args[0]!r}") from error
