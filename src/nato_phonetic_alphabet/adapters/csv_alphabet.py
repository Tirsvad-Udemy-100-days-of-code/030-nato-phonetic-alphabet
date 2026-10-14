"""@brief Adapter that reads the NATO alphabet from a CSV file."""

import csv
from importlib import resources
from importlib.resources.abc import Traversable

from nato_phonetic_alphabet import constants


def packaged_data_file() -> Traversable:
    """@brief Locate the data file shipped with the package.

    @return The packaged CSV file.
    """
    return (
        resources.files(constants.DATA_PACKAGE)
        / constants.DATA_DIRECTORY
        / constants.DATA_FILE_NAME
    )


def load_nato_dict(path: Traversable | None = None) -> dict[str, str]:
    """@brief Read the NATO alphabet from a CSV file.

    @param path The CSV file; the packaged file when omitted.
    @return Code word per upper-case letter.
    """
    source = path if path is not None else packaged_data_file()
    with source.open("r", encoding=constants.DATA_ENCODING) as stream:
        return {
            row[constants.LETTER_COLUMN].upper(): row[constants.CODE_COLUMN]
            for row in csv.DictReader(stream)
        }
