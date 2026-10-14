import subprocess
import sys

from nato_phonetic_alphabet import constants


def _run_module(stdin_text: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "nato_phonetic_alphabet"],
        input=stdin_text,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )


def test_python_dash_m_spells_word_from_piped_input() -> None:
    result = _run_module("Hi\n")

    assert result.returncode == 0
    assert constants.RESULT_TEXT in result.stdout
    assert result.stdout.splitlines()[-2:] == ["Hotel", "India"]


def test_python_dash_m_exits_cleanly_on_end_of_input() -> None:
    result = _run_module("")

    assert result.returncode == 0
    assert result.stderr == ""
