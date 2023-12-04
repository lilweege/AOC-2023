FILE = "input/04.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

lines = [line.strip() for line in FILE.readlines()]

ans = 0
cnts = [1] * len(lines)
for ln, line in enumerate(lines):
    win, nums = line.split(": ")[1].split(" | ")
    win = set(map(int, win.split()))
    nums = map(int, nums.split())
    cnt = sum(x in win for x in nums)

    if cnt:
        for i in range(ln+1, ln+cnt+1):
            cnts[i] += cnts[ln]
        ans += 1 << (cnt-1)

print(ans)
print(sum(cnts))

