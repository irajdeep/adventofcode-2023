def allq(ss) -> bool:
    for ch in ss:
        if not (ch == "?" or ch == "#"): return False
    return True

def dp(ss, l, arr, posa) -> int:
    # print(l, posa)
    if l >= len(ss):
        return posa >= len(arr)

    if posa >= len(arr):
       if "#" not in ss[l:]: return True
       return False

    ans = 0
    count = arr[posa]
    r = l + count


    if r <= len(ss) and allq(ss[l : r]) and (r >= len(ss) or ss[r] != "#"):
        ans += dp(ss, r + 1, arr, posa + 1)

    if ss[l] != "#":
        ans += dp(ss, l + 1, arr, posa)

    return ans

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]

    ans = 0
    for line in lines:
        ss, nums = line.split(" ")
        nums = [int(x) for x in nums.split(",")]
        ans += dp(ss, 0, nums, 0)

    return ans

if __name__ == "__main__":
    ans = solve1("day12.txt")
    print(ans)