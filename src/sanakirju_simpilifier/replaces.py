import re

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


def simplify_file(file: tuple[str, str]) -> tuple[str, str]:
    path, content = file
    for replace in replaces:
        content = content.replace(replace, "")

    for regex_replace in regex_replaces:
        content = re.sub(regex_replace, "", content)

    return (path, content)


def simplify_files(files: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return list(simplify_file(file) for file in files)
