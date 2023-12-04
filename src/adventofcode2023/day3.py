from adventofcode2023.utils.io import readlines


def sol1(str_matrix: list[str]) -> int:
    res = 0
    m: list[list[str]] = [ list(x) for x in str_matrix]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if _is_symbol(m[i][j]):
                res += _get_numbers(m, i, j)


    return res

def _is_symbol(c: str):
    return c != "." and not c.isdigit()

def _get_numbers(m: list[list[str]], i: int, j: int) -> int:
    i_min, i_max = 0, len(m)-1
    j_min, j_max = 0, len(m[0])-1
    modifiers = (-1,0,1)
    numbers_sum = 0
    for mi in modifiers:
        for mj in modifiers:
            curr_i = i + mi
            curr_j = j + mj
            if ((i_min <= curr_i <= i_max) 
                and (j_min <= curr_j <= j_max)):
                n = _pop_number(m, curr_i, curr_j)
                if n is not None:
                    numbers_sum += n
                    print(n)

    return numbers_sum

def _pop_number(m: list[list[str]], i: int, j: int) -> int | None:
    if not m[i][j].isdigit():
        return None
    
    j_start, j_end = j-1, j
    left_part = ""
    right_part = ""

    while j_start >= 0 and m[i][j_start].isdigit():
        left_part = f"{m[i][j_start]}{left_part}"
        m[i][j_start] = "."
        j_start -= 1

    while j_end < len(m[i]) and m[i][j_end].isdigit():
        right_part = f"{right_part}{m[i][j_end]}"
        m[i][j_end] = "."
        j_end += 1

    return int(f"{left_part}{right_part}")


if __name__ == "__main__":
    res = sol1(readlines("day3.txt"))
    print(f"sol1:", res)