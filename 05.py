FILE = "input/05.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

from collections import deque

chunks = FILE.read().strip().split("\n\n")

seeds, *chunks = chunks
seeds = list(map(int, seeds.split(": ")[1].split()))
stages = [[list(map(int, line.split())) for line in chunk.split("\n")[1:]] for chunk in chunks]


def mp(src, dst, x):
    return x - src + dst


def part1():
    ans = 1e99
    for x in seeds:
        for ranges in stages:
            for dst, src, sz in ranges:
                if src <= x < src + sz:
                    x = mp(src, dst, x)
                    break

        ans = min(ans, x)
    print(ans)


def part2_slow():
    def seed(location):
        x = location
        for ranges in reversed(stages):
            for dst, src, sz in ranges:
                if dst <= x < dst + sz:
                    x = mp(dst, src, x)
                    break
        return x

    for location in range(10**9):
        s = seed(location)
        for j in range(0, len(seeds), 2):
            if seeds[j] <= s < seeds[j] + seeds[j+1]:
                print(location)
                return


def part2():
    ans = 1e99
    for i in range(0, len(seeds), 2):
        a, b = seeds[i], seeds[i] + seeds[i+1]
        intervals = deque([(a, b)])
        for ranges in stages:
            next_intervals = []
            for dst, src, sz in ranges:
                for _ in range(len(intervals)):
                    # Inside intervals, map to new values
                    # Other values map to self (identity function)
                    #   |       start     |             |         end        |
                    #  src (1)    |      src (2)     src+sz (1)    |      src+sz (2)
                    #             |______|              |_________|
                    #                     |____________|
                    start, end = intervals.popleft()

                    first_end = min(end, src)
                    if first_end > start:
                        intervals.append((start, first_end))

                    last_start = max(start, src+sz)
                    if last_start < end:
                        intervals.append((last_start, end))

                    mid_start = max(start, src)
                    mid_end = min(src+sz, end)
                    if mid_start < mid_end:
                        next_intervals.append((
                            mp(src, dst, mid_start),
                            mp(src, dst, mid_end),
                        ))

            intervals.extend(next_intervals)
        ans = min(ans, min(intervals)[0])
    print(ans)


part1()
part2()

