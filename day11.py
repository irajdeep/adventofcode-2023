import heapq
import time

zrows, zcols = set(), set()

def all_row(r: int, lines) -> bool:
    for c in range(len(lines[0])):
        if lines[r][c] != ".":
            return False
    return True

def all_col(c: int, lines) -> bool:
    for r in range(len(lines)):
        if lines[r][c] != ".":
            return False
    return True

def dijk(src, dest, lines) -> int:
    pq, dist = [], {}
    dist[tuple(src)] = 0

    R, C = len(lines), len(lines[0])
    # src[0] = row, src[1] = col
    heapq.heappush(pq, [0, src[0], src[1]])

    while pq:

        c_dis, ur, uc = heapq.heappop(pq)
        print(c_dis, ur, uc)
        # time.sleep(1)

        if [ur, uc] == dest:
            return c_dis

        for dr, dc in [[1 , 0 ], [0, 1],[-1, 0], [0, -1]]:
            nr, nc = ur + dr, uc + dc
            if nr >= 0 and nr < R and nc >= 0 and nc < C:
                wt = 1
                if nr in zrows or nc in zcols:
                    wt = 2

                n_dis = c_dis + wt
                if tuple([nr, nc]) not in dist or dist[tuple([nr, nc])] > n_dis:
                    dist[tuple([nr, nc])] = n_dis
                    heapq.heappush(pq, [n_dis, nr, nc])

    return dist[tuple(dest)]

def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()

    lines = [line.rstrip().lstrip() for line in lines]

    points = []

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "#":
                points.append([r, c])
            if all_row(r, lines):
                zrows.add(r)
            if all_col(c, lines):
                zcols.add(c)

    ans = 0
    N = len(points)

    for n in range(N):
        for nn in range(n + 1, N):
            # use symmetry
            dr, dc = points[nn][0], points[nn][1]
            sr, sc = points[n][0], points[n][1]

            cost = 0
            for n1 in range(min(dr, sr), max(dr, sr)):
                if n1 in zrows: cost += 1000000
                else: cost += 1

            for n1 in range(min(sc, dc), max(sc, dc)):
                if n1 in zcols: cost += 1000000
                else: cost += 1

            ans += cost

    return ans


if __name__ == "__main__":
    ans = solve1("day11.txt")
    print(ans)