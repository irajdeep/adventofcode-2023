max_count = {"blue": 14, "red": 12, "green": 13}


def solve2(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()

    ans = 0
    for line in lines:
        track = {"red": 0, "blue": 0, "green": 0}
        f = line.rstrip().split(":")
        id = f[0].split(" ")[1]

        ss = f[1].lstrip()
        games =[ x.lstrip() for x in ss.split(";")]

        tmp = 1
        for g in games:
            turns = [x.lstrip() for x in g.split(",")]
            for turn in turns:
                count, color = turn.split(" ")
                track[color] = max(track[color], int(count))


            tmp = track["red"] * track["blue"] * track["green"]

        ans += tmp
    return ans


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()

    ans = 0
    for line in lines:
        possible = True
        f = line.rstrip().split(":")
        id = f[0].split(" ")[1]

        ss = f[1].lstrip()
        games =[ x.lstrip() for x in ss.split(";")]


        for g in games:
            if not possible:
                break
            turns = [x.lstrip() for x in g.split(",")]
            for turn in turns:
                count, color = turn.split(" ")
                if int(count) > max_count[color]:
                    possible = False
                    break

        if possible:
            ans += int(id)

    return ans




if __name__ == "__main__":
    ans = solve2("day2.txt")
    print(ans)