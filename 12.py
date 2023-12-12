FILE = "input/12.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

from functools import cache

lines = [line.strip() for line in FILE.readlines()]


def solve(repeat):
    ans = 0
    for line in lines:
        line, runs = line.split()
        runs = list(map(int, runs.split(",")))


        line = "?".join(line for _ in range(repeat))
        runs *= repeat

        # Simplify logic by always having a terminating .
        line += '.'

        @cache
        def dfs(lineIdx, runIdx, runLen):
            if runIdx >= len(runs):
                return all(c == '.' or c == '?' for c in line[lineIdx:])
            if lineIdx == len(line):
                return 0

            cnt = 0
            x = line[lineIdx]

            if x != '#':
                if runLen == 0:
                    cnt += dfs(lineIdx + 1, runIdx, 0)
                elif runLen == runs[runIdx]:
                    cnt += dfs(lineIdx + 1, runIdx + 1, 0)

            if x != '.':
                if runLen + 1 <= runs[runIdx]:
                    cnt += dfs(lineIdx + 1, runIdx, runLen + 1)

            return cnt

        ans += dfs(0, 0, 0)

    return ans


print(solve(1))
print(solve(5))

