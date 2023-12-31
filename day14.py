import heapq

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().lstrip() for line in lines]

    ans = 0
    # print(lines)
    R, C = len(lines), len(lines[0])

    for c in range(C):
        pos = []
        for r in range(R):
            if lines[r][c] == "O":
                if pos:
                    next = heapq.heappop(pos)
                    heapq.heappush(pos, r)
                else:
                    next = r
                ans += (R - next)
                # print(R - next)
            elif lines[r][c] == ".":
                heapq.heappush(pos, r)
            else:
                pos.clear()
    return ans


if __name__ == "__main__":
    ans = solve1("day14.txt")
    print(ans)