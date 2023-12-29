import copy

def allq(ss) -> bool:
    for ch in ss:
        if not (ch == "?" or ch == "#"): return False
    return True

def extent_s(s: str) -> str:
    curr = s
    n = 1

    while n <= 4:
        s += "?"
        s += curr
        n += 1

    return s


def extend_arr(arr: list[int]) -> list[int]:
    curr = copy.deepcopy(arr)
    n = 1

    while n <= 4:
        arr.extend(curr)
        n += 1
    return arr


def dp(ss, l, arr, posa, DP) -> int:
    if l >= len(ss):
        return posa >= len(arr)

    if posa >= len(arr):
       if "#" not in ss[l:]: return True
       return False

    if(l, posa) in DP: return DP[(l, posa)]

    ans = 0
    count = arr[posa]
    r = l + count


    if r <= len(ss) and allq(ss[l : r]) and (r >= len(ss) or ss[r] != "#"):
        ans += dp(ss, r + 1, arr, posa + 1, DP)

    if ss[l] != "#":
        ans += dp(ss, l + 1, arr, posa, DP)

    DP[(l, posa)] = ans
    return DP[(l, posa)]

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]

    ans = 0
    for line in lines:
        ss, nums = line.split(" ")
        nums = [int(x) for x in nums.split(",")]
        # print(extent_s(ss), extend_arr(nums))
        DP = {}
        ans += dp(extent_s(ss), 0, extend_arr(nums), 0, DP)

    return ans

if __name__ == "__main__":
    ans = solve1("day12.txt")
    print(ans)