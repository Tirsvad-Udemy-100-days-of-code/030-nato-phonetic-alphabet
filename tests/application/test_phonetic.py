import pytest

from nato_phonetic_alphabet.application.phonetic import generate_phonetic
from nato_phonetic_alphabet.application.ports import InputClosedError

ALPHABET = {"A": "Alfa", "B": "Bravo"}


class FakeConsole:
    def __init__(self, words: list[str]) -> None:
        self._words = words
        self.asked = 0
        self.invalid = 0

    def ask_word(self) -> str:
        self.asked += 1
        if not self._words:
            raise InputClosedError
        return self._words.pop(0)

    def show_invalid(self) -> None:
        self.invalid += 1

    def show_code_words(self, code_words: list[str]) -> None:
        raise AssertionError("generate_phonetic must not print the result")


def test_generate_phonetic_returns_code_words_for_valid_word() -> None:
    console = FakeConsole(["ab"])

    assert generate_phonetic(ALPHABET, console) == ["Alfa", "Bravo"]
    assert console.asked == 1
    assert console.invalid == 0


def test_generate_phonetic_asks_again_after_invalid_words() -> None:
    console = FakeConsole(["a1", "", "b"])

    assert generate_phonetic(ALPHABET, console) == ["Bravo"]
    assert console.invalid == 2
    assert console.asked == 3


def test_generate_phonetic_lets_closed_input_escape() -> None:
    console = FakeConsole(["x"])

    with pytest.raises(InputClosedError):
        generate_phonetic(ALPHABET, console)
    assert console.invalid == 1
