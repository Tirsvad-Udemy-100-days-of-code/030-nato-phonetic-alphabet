import pytest

from nato_phonetic_alphabet import constants
from nato_phonetic_alphabet.adapters.console import TerminalConsole
from nato_phonetic_alphabet.application.ports import InputClosedError
from nato_phonetic_alphabet.main import main


def _feed(monkeypatch: pytest.MonkeyPatch, answers: list[str]) -> list[str]:
    prompts: list[str] = []

    def fake_input(prompt: str = "") -> str:
        prompts.append(prompt)
        if not answers:
            raise EOFError
        return answers.pop(0)

    monkeypatch.setattr("builtins.input", fake_input)
    return prompts


def test_main_prints_code_words_for_valid_word(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _feed(monkeypatch, ["Hello"])

    status = main()

    lines = capsys.readouterr().out.splitlines()
    assert status == constants.EXIT_OK
    assert lines == [constants.RESULT_TEXT, "Hotel", "Echo", "Lima", "Lima", "Oscar"]


def test_main_asks_again_after_invalid_word(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    prompts = _feed(monkeypatch, ["h3llo", "Hi"])

    main()

    lines = capsys.readouterr().out.splitlines()
    assert prompts == [constants.PROMPT_TEXT, constants.PROMPT_TEXT]
    assert lines == [
        constants.INVALID_INPUT_TEXT,
        constants.RESULT_TEXT,
        "Hotel",
        "India",
    ]


def test_main_ends_cleanly_on_end_of_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _feed(monkeypatch, [])

    status = main()

    assert status == constants.EXIT_OK
    assert capsys.readouterr().out == ""


def test_terminal_console_raises_input_closed_on_interrupt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def interrupted(prompt: str = "") -> str:
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", interrupted)

    with pytest.raises(InputClosedError):
        TerminalConsole().ask_word()
