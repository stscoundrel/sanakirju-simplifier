from os.path import exists
from os import remove
from src.sanakirju_simpilifier import writer, reader


def test_lists_xml_files() -> None:
    files = reader.read_xml_files()
    results = writer.get_write_paths(files)

    # Randoly picket entries from different folders should be present in "build" format.
    expected_paths = (
        "sanakirju_simpilifier/build/kksxml/kks4/10_pol.xml",
        "sanakirju_simpilifier/build/kksxml/kks2/03_katsa.xml",
        "sanakirju_simpilifier/build/kksxml/kks6/19_vuos.xml",
    )

    assert len(results) == 90

    for expected_path in expected_paths:
        assert any(expected_path in path for path, _ in results)


def test_writes_files_to_build():
    files = reader.read_xml_files()
    destinations = writer.get_write_paths(files)

    # Files should not exist beforehand.
    for destination, _ in destinations:
        if exists(destination):
            remove(destination)

    for destination, _ in destinations:
        assert not exists(destination)

    # Just save unedited, freshly opened files in new location.
    writer.write_files(files)

    # Files should now exist
    for destination, _ in destinations:
        assert exists(destination)
