import functools
strength = { "A":13,
             "K":12,
             "Q":11,
             "T":9,
             "9":8,
             "8":7,
             "7":6,
             "6":5,
             "5":4,
             "4":3,
             "3":2,
             "2":1,
             "J":0
        }

def cmp(a, b):
    cnta, cntb = [], []

    sa = "".join(sorted(a))
    sb = "".join(sorted(b))

    sa = sa.replace("J", "")
    sb = sb.replace("J", "")

    cnt = 1
    if len(sa) == 0: cnt = 0

    for n in range(1,len(sa)):
        if sa[n] != sa[n - 1]:
            cnta.append(cnt)
            cnt = 1
        else:
            cnt += 1
    cnta.append(cnt)

    cnt = 1
    if len(sb) == 0: cnt = 0
    for n in range(1,len(sb)):
        if sb[n] != sb[n - 1]:
            cntb.append(cnt)
            cnt = 1
        else:
            cnt += 1
    cntb.append(cnt)

    cnta.sort(reverse=True)
    cntb.sort(reverse=True)

    # refine the Js now
    cnta[0] += (5 - len(sa))
    cntb[0] += (5 - len(sb))

    # print("here")
    # print(a, sa, cnta)
    # print(b, cntb)

    if len(cnta) < len(cntb):
        return 1
    elif len(cntb) < len(cnta):
        return -1
    elif cnta != cntb:
        for n in range(len(cnta)):
            if cnta[n] > cntb[n]:
                return 1
            elif cntb[n] > cnta[n]:
                return -1
    else:
        for n in range(5):
            if strength[a[n]] > strength[b[n]]:
                return 1
            elif strength[b[n]] > strength[a[n]]:
                return -1


def solve1(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    hands, hand_to_bid = [], {}

    for line in lines:
        ll = line.split(" ")
        hands.append(ll[0])
        hand_to_bid[ll[0]] = int(ll[1])

    hands.sort(key=functools.cmp_to_key(cmp))

    # print(hands)
    ans = 0
    for n, e in enumerate(hands):
        # print(e, len(e))
        ans += (n + 1) * hand_to_bid[e]
    return ans

if __name__ == "__main__":
    ans = solve1("day7.txt")
    print(ans)