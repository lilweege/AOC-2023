FILE = "input/06.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

from math import prod

lines = [s.strip() for s in FILE.readlines()]


def bisect_pred(lo, hi, ok):
    while lo < hi:
        mi = (lo + hi) // 2
        if ok(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo


def solve_one(time, dist):
    m = time // 2
    l = bisect_pred(0, m, lambda wait: (time-wait) * wait < dist)
    h = bisect_pred(m, time, lambda wait: (time-wait) * wait > dist)
    return h - l


def part1():
    time = list(map(int, lines[0].split(":")[1].strip().split()))
    dist = list(map(int, lines[1].split(":")[1].strip().split()))
    ans = prod(solve_one(t, d) for t, d in zip(time, dist))
    print(ans)


def part2():
    time = int(''.join(lines[0].split(":")[1].strip().split()))
    dist = int(''.join(lines[1].split(":")[1].strip().split()))
    ans = solve_one(time, dist)
    print(ans)


part1()
part2()

