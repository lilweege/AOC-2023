from collections import defaultdict

FILE = "input/03.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

lines = [line.strip() for line in FILE.readlines()]


def has_adj(a, b):
    for digidx in range(a, b+1):
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                i = ln+di
                j = digidx+dj
                if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                    if not lines[i][j].isdigit() and lines[i][j] != '.':
                        return (i, j)
    return None


def update():
    global a, b, ans
    if a != -1:
        adj = has_adj(a, b)
        if adj:
            n = int(line[a:b+1])
            nums[adj].add(n)
            ans += n
        a = b = -1


nums = defaultdict(set)
ans = 0
for ln, line in enumerate(lines):
    a = b = -1
    for i, c in enumerate(line):
        if c.isdigit():
            if a == -1:
                a = i
            b = i
        else: update()
    update()

print(ans)

ans = 0
for (i, j), v in nums.items():
    if len(v) != 2: continue
    a, b = v
    if lines[i][j] == '*':
        ans += a * b

print(ans)

