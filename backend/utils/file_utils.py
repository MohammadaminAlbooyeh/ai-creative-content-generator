import os
from pathlib import Path


def ensure_dir(path: str) -> Path:
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def list_files(directory: str, extension: str = None) -> list[str]:
    files = os.listdir(directory)
    if extension:
        files = [f for f in files if f.endswith(extension)]
    return sorted(files)


def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()


def write_file(filepath: str, content: str):
    with open(filepath, "w") as f:
        f.write(content)
