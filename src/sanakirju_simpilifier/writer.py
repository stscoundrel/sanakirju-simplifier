from os.path import exists
from os import remove, makedirs


def get_file_output_folder(file: str) -> str:
    return file.rsplit("/", 1)[0]


def get_write_paths(files: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return list(
        (file.replace("resources", "build"), content) for file, content in files
    )


def write_files(files: list[tuple[str, str]]) -> None:
    write_files = get_write_paths(files)

    # Remove old build, if present.
    for destination, _ in write_files:
        if exists(destination):
            remove(destination)

    for file_path, content in write_files:
        folder_path = get_file_output_folder(file_path)
        if not exists(folder_path):
            makedirs(folder_path)

        file = open(file_path, "w")
        file.write(content)
        file.close()
