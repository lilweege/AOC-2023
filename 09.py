FILE = "input/09.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

from itertools import pairwise

lines = [list(map(int, line.strip().split())) for line in FILE.readlines()]

def nxt(s):
    if all(x == 0 for x in s): return 0
    ns = [b - a for a, b in pairwise(s)]
    return s[-1] + nxt(ns)


def part1():
    print(sum(nxt(line) for line in lines))


def part2():
    print(sum(nxt(line[::-1]) for line in lines))


part1()
part2()

