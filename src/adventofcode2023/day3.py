from copy import deepcopy
from typing import Any, Generator
from adventofcode2023.utils.io import readlines


def sol1(str_matrix: list[str]) -> int:
    res = 0

    # Transform input into matrix, aka list of lists
    m: list[list[str]] = [list(x) for x in str_matrix]

    # Traverse the matrix in order
    for c, i, j in _traverse_matrix(m):
        if c.isdigit():
            res += _pop_number(m, i, j)

    return res


def sol2(str_matrix: list[str]) -> int:
    res = 0

    # Transform input into matrix, aka list of lists
    m: list[list[str]] = [list(x) for x in str_matrix]

    # Traverse the matrix in order
    for c, i, j in _traverse_matrix(m):
        if c == "*":
            numbers = _get_numbers_around(m, i, j)
            if len(numbers) == 2:
                res += numbers[0] * numbers[1]
    return res


## Aux functions

def _get_numbers_around(m: list[list[str]], i: int, j: int) -> list[int]:
    modifiers = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    m_copy = deepcopy(m)
    numbers = []
    for modifier_i, modifier_j in modifiers:
        i_curr = i + modifier_i
        j_curr = j + modifier_j

        if m_copy[i_curr][j_curr].isdigit():
            n = _pop_number(m_copy, i_curr, j_curr)
            if n != 0:
                numbers.append(n)

    return numbers


def _traverse_matrix(m: list[list[str]]):
    """Returns char, i, j"""
    for i in range(len(m)):
        for j in range(len(m[0])):
            yield m[i][j], i, j


def _is_symbol(c: str):
    return c != "." and not c.isdigit()


def _pop_number(m: list[list[str]], i: int, j: int) -> int:
    j_start, j_end = j - 1, j
    left_part = ""
    right_part = ""

    adjacent_symbols = []

    while j_start >= 0 and m[i][j_start].isdigit():
        left_part = f"{m[i][j_start]}{left_part}"
        m[i][j_start] = "."
        adjacent_symbols.extend(_get_adjacent_symbols(m, i, j_start, mode="up down"))
        j_start -= 1
    adjacent_symbols.extend(_get_adjacent_symbols(m, i, j_start + 1, mode="left side"))

    while j_end < len(m[i]) and m[i][j_end].isdigit():
        right_part = f"{right_part}{m[i][j_end]}"
        m[i][j_end] = "."
        adjacent_symbols.extend(_get_adjacent_symbols(m, i, j_end, mode="up down"))
        j_end += 1
    adjacent_symbols.extend(_get_adjacent_symbols(m, i, j_end - 1, mode="right side"))

    if len(adjacent_symbols) == 0:
        return 0

    return int(f"{left_part}{right_part}")


def _get_adjacent_symbols(m: list[list[str]], i: int, j: int, mode: str) -> list[str]:
    if mode == "up down":
        modifiers = [(1, 0), (-1, 0)]

    elif mode == "left side":
        modifiers = [(1, -1), (-1, -1), (0, -1)]

    elif mode == "right side":
        modifiers = [(1, 1), (-1, 1), (0, 1)]
    else:
        raise ValueError(f"Invalid mode {mode}")

    symbols = []
    for modifier_i, modifier_j in modifiers:
        i_curr = i + modifier_i
        j_curr = j + modifier_j
        # Check if valid coordinate and is symbol
        if (
            len(m) > i_curr >= 0
            and len(m[0]) > j_curr >= 0
            and _is_symbol(m[i_curr][j_curr])
        ):
            symbols.append(m[i_curr][j_curr])

    return symbols


if __name__ == "__main__":
    res = sol1(readlines("day3.txt"))
    print(f"sol1:", res)
    res = sol2(readlines("day3.txt"))
    print(f"sol2:", res)
