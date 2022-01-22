from os.path import dirname
import glob
from .types import Files, FilePath

resource_path = dirname(__file__) + "/resources/kksxml/"


def list_xml_files() -> list[FilePath]:
    return list(
        filename
        for filename in glob.iglob(str(resource_path) + "**/*.xml", recursive=True)
    )


def read_xml_files() -> Files:
    files = list_xml_files()

    return list((file, open(file).read()) for file in files)
