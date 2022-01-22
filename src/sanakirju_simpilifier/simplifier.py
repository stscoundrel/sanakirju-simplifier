from . import reader, replaces, writer


def simplify_sanakirju() -> None:
    source_files = reader.read_xml_files()
    output_files = replaces.simplify_files(source_files)

    writer.write_files(output_files)
