from adventofcode2023.utils.io import process_input
import re

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

# aux functions

def _get_id(game: str) -> int:
    r = re.match(r"Game (\d+):", game)
    if not r:
        raise ValueError(f"Game with wrong format: {game}")
    return int(r.group(1))

def _get_rounds(game: str):
    str_rounds = game.split(":")[-1].split(";")
    for str_round in str_rounds:
        d = {}
        for show in [ x.strip() for x in str_round.split(",") ]:
            _tmp = show.split(" ")
            n = int(_tmp[0])
            color = _tmp[1]
            d[color] = n
        yield d

if __name__ == "__main__":
    res = process_input("day2.txt", sol1)
    res = map(int, res)
    print(f"sol1:",sum(res))
