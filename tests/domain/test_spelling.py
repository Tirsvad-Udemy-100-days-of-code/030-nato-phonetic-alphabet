import pytest

from nato_phonetic_alphabet.adapters.csv_alphabet import load_nato_dict
from nato_phonetic_alphabet.domain.spelling import InvalidWordError, spell_word

ALPHABET = load_nato_dict()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@pytest.mark.parametrize("letter", list(LETTERS))
def test_spell_word_maps_letter_to_its_code_word(letter: str) -> None:
    assert spell_word(letter, ALPHABET) == [ALPHABET[letter]]


def test_spell_word_uses_known_code_words() -> None:
    assert spell_word("ADZ", ALPHABET) == ["Alfa", "Delta", "Zulu"]


def test_spell_word_covers_all_26_letters() -> None:
    assert len(spell_word(LETTERS, ALPHABET)) == len(LETTERS)


def test_spell_word_is_case_insensitive_for_mixed_case() -> None:
    assert spell_word("Hello", ALPHABET) == [
        "Hotel",
        "Echo",
        "Lima",
        "Lima",
        "Oscar",
    ]


@pytest.mark.parametrize("word", ["a1", "two words", "hi!", "", "ß", "æ"])
def test_spell_word_raises_for_non_letter_or_empty(word: str) -> None:
    with pytest.raises(InvalidWordError):
        spell_word(word, ALPHABET)


def test_spell_word_keeps_cause_of_invalid_character() -> None:
    with pytest.raises(InvalidWordError) as info:
        spell_word("a1", ALPHABET)

    assert isinstance(info.value.__cause__, KeyError)
