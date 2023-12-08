FILE = "input/08.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

import math

lines = [line.strip() for line in FILE.readlines()]
walk, _, *lines = lines

adj = {}
for ln, line in enumerate(lines):
    fr, to = line.split(" = ")
    adj[fr] = to[1:-1].split(", ")


def findlen(src, done):
    curr = src
    step = 0
    while not done(curr):
        dir = 0 if walk[step % len(walk)] == "L" else 1
        curr = adj[curr][dir]
        step += 1
    return step


def part1():
    print(findlen("AAA", lambda s: s == "ZZZ"))


def part2():
    print(math.lcm(*(findlen(src, lambda s: s[-1] == "Z")
        for src in adj.keys() if src[-1] == "A")))


part1()
part2()

