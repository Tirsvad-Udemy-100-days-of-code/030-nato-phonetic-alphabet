"""@brief Adapter that reads the NATO alphabet from a CSV file."""

import csv
import importlib
from typing import Literal, Protocol, TextIO, cast

from nato_phonetic_alphabet import constants


class Traversable(Protocol):
    """@brief A readable file or directory, such as a path or a packaged resource."""

    def __truediv__(self, child: str) -> "Traversable":
        """@brief Return the child with the given name.

        @param child The name of the child.
        @return The child.
        """
        ...

    def open(self, mode: Literal["r"], *, encoding: str) -> TextIO:
        """@brief Open the file for reading text.

        @param mode The mode, always "r".
        @param encoding The text encoding.
        @return The open text stream.
        """
        ...


def packaged_data_file() -> Traversable:
    """@brief Locate the data file shipped with the package.

    @return The packaged CSV file.
    """
    resources = importlib.import_module("importlib.resources")
    root = cast(Traversable, resources.files(constants.DATA_PACKAGE))
    return root / constants.DATA_DIRECTORY / constants.DATA_FILE_NAME


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
