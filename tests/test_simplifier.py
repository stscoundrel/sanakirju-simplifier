from os.path import exists
from os import remove
from src.sanakirju_simpilifier import simplifier, reader, writer
from src.sanakirju_simpilifier.types import Files


def setup_tests(destinations: Files):
    files = reader.read_xml_files()
    destinations = writer.get_write_paths(files)

    # Files should not exist beforehand.
    for destination, _ in destinations:
        if exists(destination):
            remove(destination)

    for destination, _ in destinations:
        assert not exists(destination)


def test_creates_simplified_version_of_dataser():
    files = reader.read_xml_files()
    destinations = writer.get_write_paths(files)
    setup_tests(destinations)

    simplifier.simplify_sanakirju()

    # Assert files were created
    for destination, _ in destinations:
        assert exists(destination)
