"""@brief Composition root: wires the adapters into the use case."""

from nato_phonetic_alphabet import constants
from nato_phonetic_alphabet.adapters.console import TerminalConsole
from nato_phonetic_alphabet.adapters.csv_alphabet import load_nato_dict
from nato_phonetic_alphabet.application.phonetic import generate_phonetic
from nato_phonetic_alphabet.application.ports import InputClosedError
from nato_phonetic_alphabet.domain.spelling import InvalidWordError, spell_word

__all__ = [
    "InvalidWordError",
    "generate_phonetic",
    "load_nato_dict",
    "main",
    "spell_word",
]


def main() -> int:
    """@brief Run the interactive tool.

    Ends without a result when the user can give no more input.

    @return The exit status of the program.
    """
    console = TerminalConsole()
    try:
        code_words = generate_phonetic(load_nato_dict(), console)
    except InputClosedError:
        return constants.EXIT_OK
    console.show_code_words(code_words)
    return constants.EXIT_OK
