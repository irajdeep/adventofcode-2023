def all(arr):
    return max(arr) == min(arr) and max(arr) == 0


def solve(arr: list[int]) -> int:
    tmp = []
    tmp.append(arr)

    while True:
        if all(arr):
            break
        curr = []
        for n in range(1, len(arr)):
            curr.append(arr[n] - arr[n - 1])

        arr = curr
        tmp.append(arr)

    # print(tmp)
    # last_elm = 0
    prev_elm = 0
    for e in reversed(tmp[:-1]):
        # print(e)
        prev_elm = e[0] - prev_elm

    # print(last_elm)
    # print(prev_elm)
    return prev_elm


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]

    arrs = []

    for line in lines:
        tmp = [int(x) for x in line.split(" ")]
        arrs.append(tmp)

    # print(arrs)
    ans = 0
    for arr in arrs:
        ans += solve(arr)

    return ans



if __name__ == "__main__":
    ans = solve1("day9.txt")
    print(ans)