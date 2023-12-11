FILE = "input/10.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

grid = [[c for c in line.strip()] for line in FILE.readlines()]

def ok(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S":
            si, sj = i, j

R = (0, 1)
D = (1, 0)
L = (0, -1)
U = (-1, 0)
dirs = [R, D, L, U]
mp = {
    "|": [U, D],
    "-": [L, R],
    "L": [U, R],
    "J": [U, L],
    "7": [D, L],
    "F": [D, R],
}
R, D, L, U = 0, 1, 2, 3
starts = {
    (D, U): "|",
    (R, L): "-",
    (R, U): "L",
    (L, U): "J",
    (R, D): "F",
    (D, L): "7",
}

sides = [""] * 4
for s, dirlst in mp.items():
    for d in dirlst:
        sides[dirs.index(d)] += s

startdirs = []
for idx, ((di, dj), side) in enumerate(zip(dirs, sides[2:]+sides[:2])):
    i, j = si + di, sj + dj
    if ok(i, j) and grid[i][j] in side:
        startdirs.append(idx)
assert len(startdirs) == 2

path = set([(si, sj)])
di, dj = dirs[startdirs[0]]
pi, pj, i, j = si, sj, si+di, sj+dj
while (i, j) != (si, sj):
    path.add((i, j))
    (di, dj), (di2, dj2) = mp[grid[i][j]]
    if (i+di, j+dj) == (pi, pj):
        di, dj = di2, dj2
    pi, pj, i, j = i, j, i+di, j+dj
print(len(path) // 2)


grid[si][sj] = starts[tuple(startdirs)]
ans = 0
for i in range(len(grid)):
    pipes = 0
    for j in range(len(grid[0])):
        if (i, j) in path:
            if grid[i][j] in sides[D]:
                pipes += 1
        else:
            ans += pipes & 1
print(ans)

