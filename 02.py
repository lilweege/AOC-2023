FILE = "input/02.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

lines = FILE.readlines()

def part1():
    ans = 0
    for idx, line in enumerate(lines, 1):
        sets = line.strip().split(": ")[1].split("; ")
        poss = True
        for s in sets:
            r = g = b = 0
            for p in s.split(", "):
                n, c = p.split()
                n = int(n)
                if c[0] == 'g': g += n
                if c[0] == 'b': b += n
                if c[0] == 'r': r += n
            if r > 12 or g > 13 or b > 14:
                poss = False
        if poss:
            ans += idx
    print(ans)


def part2():
    ans = 0
    for line in lines:
        sets = line.strip().split(": ")[1].split("; ")
        r = g = b = 0
        for s in sets:
            for p in s.split(", "):
                n, c = p.split()
                n = int(n)
                if c[0] == 'g': g = max(g, n)
                if c[0] == 'b': b = max(b, n)
                if c[0] == 'r': r = max(r, n)
        p = r * g * b
        ans += p
    print(ans)


part1()
part2()

