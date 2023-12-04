import sys
from typing import Callable, Literal
from pathlib import Path

from adventofcode2023 import root_dir

def process_input(input_file_name: str, func: Callable[[str],int]) -> int:
    """input file needs to exist"""
    
    try:
        f_input = open(_get_file_path(input_file_name, file_type="input"))
        f_output = open(_get_file_path(f"solution_{input_file_name}", file_type="output"), "+w")

    except OSError as e:
        print(f"Error reading {input_file_name}: {e}")
        sys.exit(-1)

    res = 0
    for line in f_input.readlines():
        sol = func(line.rstrip("\n"))
        f_output.write(str(sol)+"\n")
        res+=sol

    f_input.close()
    f_output.close()
    print(f"'{input_file_name}' Processed with {func.__name__}!")
    return res


def readlines(input_file_name: str) -> list[str]:
    with open(_get_file_path(input_file_name, file_type="input")) as f:
        lines = [x.rstrip("\n") for x in f.readlines()]
    return lines

# aux functions
def _get_file_path(input_file_name: str, file_type: Literal["input"]| Literal["output"]) -> Path:
    if file_type not in ["input", "output"]:
        raise ValueError(f"{file_type = } is not valid")
    
    return root_dir / f"{file_type}s" / input_file_name

