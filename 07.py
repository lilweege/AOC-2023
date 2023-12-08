FILE = "input/07.txt"
# FILE = "sample.txt"
FILE = open(FILE, "r")

from collections import Counter

lines = [line.strip() for line in FILE.readlines()]

strength1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strength2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def score(cnt):
    if cnt.most_common(1)[0][1] == 5:
        return 6
    if cnt.most_common(1)[0][1] == 4:
        return 5
    if cnt.most_common(1)[0][1] == 3 and cnt.most_common(2)[1][1] == 2:
        return 4
    if cnt.most_common(1)[0][1] == 3:
        return 3
    if len(cnt) == 3:
        return 2
    if len(cnt) == 4:
        return 1
    return 0


def part1():
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((score(Counter(hand)), [-strength1.index(c) for c in hand], int(bid)))

    print(sum(i * bid for i, (*_, bid) in enumerate(sorted(hands), 1)))


def part2():
    hands = []
    for line in lines:
        hand, bid = line.split()

        cnt = Counter(hand)
        if hand == "J" * 5:
            cnt = Counter("A" * 5)

        j = cnt["J"]
        cnt["J"] = 0
        cnt[cnt.most_common()[0][0]] += j
        cnt.pop("J")

        hands.append((score(cnt), [-strength2.index(c) for c in hand], int(bid)))

    print(sum(i * bid for i, (*_, bid) in enumerate(sorted(hands), 1)))


part1()
part2()

