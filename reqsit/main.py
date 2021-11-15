import glob
from fire import Fire
from art import tprint
from typing import List
import errno
import os


def find_reqs(filename: str) -> str:
    """Find the path of the first requirements.txt."""
    paths = glob.glob("**/" + filename, recursive=True)
    if len(paths) > 0:
        return paths[0]
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)


def read_reqs(filename: str) -> List[str]:
    """Read requirements line-by-line into a list."""
    with open(filename, "r") as f:
        contents = f.readlines()

    return contents


def convert_reqs(reqs: List[str]) -> List[str]:
    """Convert each line into the format for pyproject.toml."""
    conversion = []
    for req in reqs:
        req = req.replace("\n", '",')
        conversion.append(f'"{req}')
    return conversion


def display_reqs(reqs: List[str]) -> List[str]:
    """Print the lines to the console."""
    tprint("reqsit")
    return reqs


def fire_wrapper(filename="requirements.txt") -> List[str]:
    path = find_reqs(filename)
    contents = read_reqs(path)
    reqs = convert_reqs(contents)
    return display_reqs(reqs)


def main() -> None:
    Fire(fire_wrapper)


if __name__ == "__main__":
    main()
