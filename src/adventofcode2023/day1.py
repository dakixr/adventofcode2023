from adventofcode2023.utils.io import process_input

def sol1(s: str) -> int:
    i, j = 0, len(s)-1
    while not s[i].isdigit():
        i += 1
    while not s[j].isdigit():
        j -= 1
    return int(f"{s[i]}{s[j]}")

##############################################################

def sol2(s: str) -> int:
    i, j = 0, len(s)-1
    i_res = ""
    j_res = ""

    while True:

        # Digit found
        if s[i].isdigit():
            i_res = s[i]
            break

        # Word found
        str_number = _find_str_number(s[i:], GRAPH_NUMBERS)
        if str_number:
            i_res = DICT_NUMBERS[str_number]
            break

        i+=1

    while True:

        # Digit found
        if s[j].isdigit():
            j_res = s[j]
            break

        # Word found
        str_number = _find_str_number(s[j::-1], GRAPH_NUMBERS_REVERSED)
        if str_number:
            j_res = DICT_NUMBERS[str_number[::-1]]
            break

        j-=1

    return int(f"{i_res}{j_res}")


# aux functions

def _find_str_number(s: str, g: dict) -> str | None:
    curr = g
    res = ""
    for l in s:
        if len(curr)==0:
            return res
        if l not in curr:
            return None
        curr = curr[l]
        res += l
    return None


# aux datastructures

def _generate_graph(words: tuple[str, ...]) -> dict:
    d = {}
    for w in words:
        current = d
        for l in w:
            if l not in current:
                current[l] = {}
            current = current[l]
    return d

DICT_NUMBERS = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}
GRAPH_NUMBERS = _generate_graph(tuple(DICT_NUMBERS.keys()))
GRAPH_NUMBERS_REVERSED = _generate_graph(tuple(x[::-1] for x in tuple(DICT_NUMBERS.keys())))

if __name__ == "__main__":
    res = process_input("day1.txt", sol1)
    print(f"sol1:",res)

    res = process_input("day1.txt", sol2)
    print(f"sol2:",res)

