def is_digit(s: str) -> int:
    if s.isdigit():
        return int(s)

    numbers = {"one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "seven": 7,
               "eight": 8,
               "nine": 9
               }

    if s in numbers:
        return numbers[s]
    return None

def solve2(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()

    ans = 0
    for line in lines:
        seen = False
        first, last = -1, -1
        for pos, ch in enumerate(line):
            # print(pos, ch)
            o1, o2, o3, o4 = is_digit(ch), is_digit(line[pos:pos + 3]), is_digit(line[pos:pos + 4]), is_digit(line[pos:pos + 5])

            if o1 is not None:
                if not seen:
                    seen = True
                    first = o1

            if o2 is not None:
                if not seen:
                    seen = True
                    first = o2

            if o3 is not None:
                if not seen:
                    seen = True
                    first = o3

            if o4 is not None:
                if not seen:
                    seen = True
                    first = o4

            if o4 is not None:
                last = o4

            if o3 is not None:
                last = o3

            if o2 is not None:
                last = o2

            if o1 is not None:
                last = o1

        print(10*first + last)
        ans += 10*first + last

    return ans


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()


    ans = 0
    for line in lines:
        seen = False
        first, last = -1, -1
        for ch in line:
            if ch.isdigit() and not seen:
                seen = True
                first = int(ch)
            if ch.isdigit():
                last = int(ch)

        # print(10*first + last)
        ans += 10*first + last
        # print(ans)
    return ans


if __name__ == "__main__":
    ans = solve2("day1.txt")
    print(ans)