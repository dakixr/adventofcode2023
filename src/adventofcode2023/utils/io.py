import sys
from typing import Callable
from adventofcode2023 import root_dir

def process_input(input_file_name: str, func: Callable):
    """input file needs to exist"""
    
    try:
        f_input = open(root_dir / "inputs" / input_file_name)
        f_output = open(root_dir / "outputs" / f"solution_{input_file_name}", "+w")

    except OSError as e:
        print(f"Error reading {input_file_name}: {e}")
        sys.exit(-1)

    for line in f_input.readlines():
        f_output.write(func(line.rstrip("\n"))+"\n")

    print(f"'{input_file_name}' Processed!")
