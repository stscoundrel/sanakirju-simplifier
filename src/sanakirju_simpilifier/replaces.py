import re
from .types import File, Files

regex_replaces = [
    "<RangeOfApplication[^>]*>",
    "<Fragment[^>]*>",
    "<SeeAlso[^>]*>",
    "<Ptr[^>]*>",
]

replaces = [
    "</RangeOfApplication>",
    "</Fragment>",
    "</SeeAlso>",
    "</Ptr>",
]


def simplify_file(file: File) -> File:
    path, content = file
    for replace in replaces:
        content = content.replace(replace, "")

    for regex_replace in regex_replaces:
        content = re.sub(regex_replace, "", content)

    return (path, content)


def simplify_files(files: Files) -> Files:
    return list(simplify_file(file) for file in files)
