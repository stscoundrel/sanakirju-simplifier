from os.path import dirname
import glob

resource_path = dirname(__file__) + "/resources/kksxml/"


def list_xml_files() -> list[str]:
    return list(
        filename
        for filename in glob.iglob(str(resource_path) + "**/*.xml", recursive=True)
    )


def read_xml_files() -> list[tuple[str, str]]:
    files = list_xml_files()

    return list((file, open(file).read()) for file in files)
