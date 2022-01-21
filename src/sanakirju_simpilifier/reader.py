from os.path import dirname
from typing import Any
import glob

root_path = dirname(__file__) + "/resources/kksxml/"


def list_xml_files() -> list[str]:
    return list(
        filename for filename in glob.iglob(str(root_path) + "**/*.xml", recursive=True)
    )
