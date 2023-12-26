from collections import defaultdict

def dfs(r: int, c: int, grid: list[list[str]], vis: list[list[str]], col: int):
    vis[r][c] = col

    for dr, dc in [[0,1], [1,0], [-1,1], [1,1], [1,-1], [0,-1], [-1,0], [-1,-1]]:
        nr, nc = r + dr, c + dc
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
            if not vis[nr][nc] and grid[nr][nc] != ".":
                dfs(nr, nc, grid, vis, col)


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    R, C = len(lines), len(lines[0])
    grid = [["." for c in range(C)] for r in range(R)]
    vis = [[0 for c in range(C)] for r in range(R)]
    sources = []

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            grid[r][c] = ch
            if not ch.isdigit() and ch != ".":
                # print(ch, r, c)
                sources.append([r, c])
    # do a dfs from each of the sources and mark it 1
    for e in sources:
        dfs(e[0], e[1], grid, vis)

    ans = 0
    for r, line in enumerate(lines):
        c = 0
        while c < len(grid[0]):
            start, end = -1, -1
            if vis[r][c] and grid[r][c].isdigit():
                start = c
                while c < len(grid[0]) and grid[r][c].isdigit():
                    c+= 1
                    end = c

            tmp = line[start:end]
            c += 1

            if tmp.isdigit():
                ans += int(tmp)
        r += 1
    return ans

def solve2(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    R, C = len(lines), len(lines[0])
    grid = [["." for c in range(C)] for r in range(R)]
    vis = [[0 for c in range(C)] for r in range(R)]
    sources = []

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            grid[r][c] = ch
            if ch == "*":
                sources.append([r, c])

    for col, e in enumerate(sources):
        dfs(e[0], e[1], grid, vis, col + 1)


    maps = defaultdict(list)
    ans = 0

    for r, line in enumerate(lines):
        c, col = 0, -1
        while c < len(grid[0]):
            col = -1
            start, end = -1, -1
            if vis[r][c] and grid[r][c].isdigit():
                col = vis[r][c]
                start = c
                while c < len(grid[0]) and grid[r][c].isdigit():
                    c+= 1
                    end = c

            tmp = line[start:end]
            c += 1

            if tmp.isdigit():
                maps[col].append(int(tmp))
        r += 1

    for k, v in maps.items():
        # print(k, v)
        if len(v) == 2:
            ans += v[0] * v[1]

    return ans


if __name__ == "__main__":
    ans = solve2("day3.txt")
    print(ans)