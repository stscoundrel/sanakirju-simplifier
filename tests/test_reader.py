from src.sanakirju_simpilifier import reader


def test_lists_xml_files() -> None:
    results = reader.list_xml_files()

    # Randoly picket entries from different folders should be present.
    expected_paths = (
        "sanakirju_simpilifier/resources/kksxml/kks4/10_pol.xml",
        "sanakirju_simpilifier/resources/kksxml/kks2/03_katsa.xml",
        "sanakirju_simpilifier/resources/kksxml/kks6/19_vuos.xml",
    )

    assert len(results) == 90

    for expected_path in expected_paths:
        assert any(expected_path in path for path in results)


def test_reads_xml_files() -> None:
    results = reader.read_xml_files()

    # Each read file should contain dictionary xml with dictionary entries.
    for _, contents in results:
        assert "<Dictionary" in contents
        assert "</Dictionary>" in contents
        assert "<DictionaryEntry" in contents
        assert "</DictionaryEntry>" in contents
