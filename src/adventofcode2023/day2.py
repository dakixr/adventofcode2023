from functools import reduce
from operator import mul
import re

from adventofcode2023.utils.io import process_input

# 12 red cubes, 13 green cubes, and 14 blue cubes
BAG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def sol1(game: str) -> int:
    for round in _get_rounds(game):
        for color, n in round.items():
            if BAG[color] < n:
                return 0
    return _get_id(game)

def sol2(game: str) -> int:
    min_needed = reduce(_keep_max_color,_get_rounds(game))
    return reduce(mul, min_needed.values())


# aux functions

def _keep_max_color(d1: dict, d2: dict) -> dict:
    """This function assumes that d1 and d2 have the same keys"""
    return { k: max(d1[k],d2[k]) for k in d1.keys()}

def _get_id(game: str) -> int:
    r = re.match(r"Game (\d+):", game)
    if not r:
        raise ValueError(f"Game with wrong format: {game}")
    return int(r.group(1))

def _get_rounds(game: str):
    """returns dict as follows -> color: n"""
    str_rounds = game.split(":")[-1].split(";")
    for str_round in str_rounds:
        d = {"red": 0,"green": 0,"blue": 0}
        for show in [ x.strip() for x in str_round.split(",") ]:
            _tmp = show.split(" ")
            n = int(_tmp[0])
            color = _tmp[1]
            d[color] = n
        yield d

if __name__ == "__main__":
    res = process_input("day2.txt", sol1)
    print(f"sol1:",res)

    res = process_input("day2.txt", sol2)
    print(f"sol2:",res)
