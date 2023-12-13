FILE = "input/13.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

chunks = FILE.read().split("\n\n")


def summarizeT(tolerance, grid):
    n = len(grid)
    for i in range(1, n):
        diff = 0
        for di in range(n):
            i1 = i - di - 1
            i2 = i + di
            if not 0 <= i1 < n or not 0 <= i2 < n:
                break
            diff += sum(a != b for a, b in zip(grid[i1], grid[i2]))

        if diff == tolerance:
            return i
    return 0


def solve(tolerance):
    return sum(
        summarizeT(tolerance, list(zip(*grid))) +
        summarizeT(tolerance, grid) * 100
        for grid in map(str.splitlines, chunks)
    )


print(solve(0))
print(solve(1))

