FILE = "input/01.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

s = FILE.read().strip()

def part1():
    ans = 0
    for l in s.split("\n"):

        first = last = 0
        for c in l:
            if c.isdigit():
                x = int(c)
                if not first:
                    first = x
                last = x

        ans += first * 10 + last

    print(ans)


def part2():
    ans = 0
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for l in s.split("\n"):

        first = last = 0
        for i, c in enumerate(l):
            x = 0
            if c.isdigit():
                x = int(c)
            else:
                for j, n in enumerate(nums, 1):
                    if l.startswith(n, i):
                        x = j
                        break

            if x:
                if not first:
                    first = x
                last = x

        ans += first * 10 + last

    print(ans)


part1()
part2()

