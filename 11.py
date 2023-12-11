FILE = "input/11.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

grid = [line.strip() for line in FILE.readlines()]

n, m = len(grid), len(grid[0])

add_vert = [0] * n
add_horz = [0] * m

for i in range(n):
    add_vert[i] = add_vert[i-1]
    if all(grid[i][j] == '.' for j in range(m)):
        add_vert[i] += 1

for j in range(m):
    add_horz[j] = add_horz[j-1]
    if all(grid[i][j] == '.' for i in range(n)):
        add_horz[j] += 1

galaxies = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            galaxies.append((i, j))

def solve(scl):
    ans = 0
    n = len(galaxies)
    for i in range(n):
        for j in range(i+1, n):
            i1, j1 = galaxies[i]
            i2, j2 = galaxies[j]
            if i1 > i2: i1, i2 = i2, i1
            if j1 > j2: j1, j2 = j2, j1
            dst = (i2 - i1) + (j2 - j1) + scl * (add_vert[i2] - add_vert[i1]) + scl * (add_horz[j2] - add_horz[j1])
            ans += dst
    return ans


print(solve(1))
print(solve(10**6 - 1))

