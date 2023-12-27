
from math import gcd
import time
def lcm(arr):
    lcm = 1
    for i in arr:
        lcm = lcm*i//gcd(lcm, i)

    return lcm

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]
    dir = lines[0]
    nav = {}
    starts = []

    for line in lines[2:]:
        ll = line.split("=")
        key = ll[0].rstrip().lstrip()

        val = ll[1].lstrip().rstrip()
        val = val[1:len(val) - 1].split(",")
        nav[key] = [val[0].lstrip().rstrip(), val[1].lstrip().rstrip()]

        if key.endswith("A"): starts.append(key)


    N = len(dir)
    ans, n = [], 0


    for s in starts:
        ns = s
        tmp = 0

        while True:
            d = dir[n % N]
            # print(ns)

            if d == "L": ns = nav[ns][0]
            else: ns = nav[ns][1]

            tmp += 1
            n += 1
            if ns.endswith("Z"): break

            # time.sleep(1)

        ans.append(tmp)

    return lcm(ans)

if __name__ == "__main__":
    ans = solve1("day8.txt")
    print(ans)