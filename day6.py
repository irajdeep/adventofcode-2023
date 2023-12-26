def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip().strip() for line in lines]

    l1, l2 = lines[0], lines[1]

    # times = [int(x) for x in l1.lstrip().split(":")[1].split(" ") if x.isdigit()]
    # distances = [int(x) for x in l2.lstrip().split(":")[1].split(" ") if x.isdigit()]

    times     = [x for x in l1.lstrip().split(":")[1].split(" ")]
    distances = [x for x in l2.lstrip().split(":")[1].split(" ")]

    T = int("".join(times))
    D = int("".join(distances))

    print(T, D)

    # ans = 1
    # for n in range(len(times)):
    #     T, D = times[n], distances[n]
    #     tmp = 0

    #     for t in range(T + 1):
    #         x = t*(T - t) - D
    #         if x > 0: tmp += 1

    #     if tmp > 0: ans *= tmp
    tmp = 0
    for t in range(T + 1):
        x = t*(T - t) - D
        if x > 0: tmp += 1

    return tmp

if __name__ == "__main__":
    ans = solve1("day6.txt")
    print(ans)