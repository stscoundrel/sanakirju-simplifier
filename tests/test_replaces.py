from src.sanakirju_simpilifier import replaces, reader


def test_replaces_simple_content_in_xml_files() -> None:
    original_files = reader.read_xml_files()
    results = replaces.simplify_files(original_files)

    # Original files should contain replacable bits.
    for _, contents in original_files:
        assert "</RangeOfApplication>" in contents
        assert "</Fragment>" in contents
        assert "</SeeAlso>" in contents
        assert "</Ptr>" in contents

    # Result should not contain replacable bits.
    for _, contents in results:
        assert "</RangeOfApplication>" not in contents
        assert "</Fragment>" not in contents
        assert "</SeeAlso>" not in contents
        assert "</Ptr>" not in contents


def test_replaces_regex_content_in_xml_files() -> None:
    original_files = reader.read_xml_files()
    results = replaces.simplify_files(original_files)

    # Original files should contain regexable bits.
    for _, contents in original_files:
        assert "<RangeOfApplication" in contents
        assert "<Fragment" in contents
        assert "<SeeAlso" in contents
        assert "<Ptr" in contents

    # Result should not contain regexable bits.
    for _, contents in results:
        assert "<RangeOfApplication" not in contents
        assert "<Fragment" not in contents
        assert "<SeeAlso" not in contents
        assert "<Ptr" not in contents
