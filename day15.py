def compute_hash(ss: str) -> int:
    res = 0
    for ch in ss:
        res += ord(ch)
        res *= 17
        res = res % 256

    return res


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    line = lines[0].rstrip().lstrip()

    ss = line.split(",")
    ans = 0
    for s in ss:
        ans += compute_hash(s)

    return ans

if __name__ == "__main__":
    ans = solve1("day15.txt")
    print(ans)