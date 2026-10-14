"""Smoke tests of the package skeleton."""

from importlib import resources

from nato_phonetic_alphabet import constants

EXPECTED_ROW_COUNT = 26


def test_data_file_exists_in_package() -> None:
    data_file = (
        resources.files(constants.DATA_PACKAGE)
        / constants.DATA_DIRECTORY
        / constants.DATA_FILE_NAME
    )

    assert data_file.is_file()


def test_data_file_has_one_row_per_letter() -> None:
    data_file = (
        resources.files(constants.DATA_PACKAGE)
        / constants.DATA_DIRECTORY
        / constants.DATA_FILE_NAME
    )

    lines = data_file.read_text(encoding="utf-8").splitlines()

    assert len(lines) - 1 == EXPECTED_ROW_COUNT
