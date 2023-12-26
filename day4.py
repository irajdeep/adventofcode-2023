import math
from collections import defaultdict

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]
    ans = 0

    count = defaultdict(int)

    for card_num, line in enumerate(lines):
        count[card_num + 1] += 1
        cnt = 0
        present = set()
        ss = line.split("|")
        pr = ss[0].split(":")[1].lstrip().rstrip()


        for e in pr.split(" "):
            if e.isdigit():
                present.add(e)

        gi = ss[1].lstrip().rstrip()

        for e in gi.split(" "):
            if e in present:
                cnt += 1


        ncount = count[card_num + 1]

        for n in range(card_num + 2, card_num + cnt + 2):
            count[n] += ncount

        # print(card_num, count)

    for k, v in count.items():
        ans += v

    return int(ans)

if __name__ == "__main__":
    ans = solve1("day4.txt")
    print(ans)