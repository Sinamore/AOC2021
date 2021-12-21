from collections import deque
from math import inf

with open('tests/15_1.input', 'r') as inp:
    risk = [[int(x) for x in line] for line in inp.read().split('\n')[:-1]]

    danger = [[inf for x in line] for line in risk]

    q = deque()
    q.append((0, 0))
    danger[0][0] = 0

    while len(q) > 0:
        x, y = q.popleft()
        if x > 0 and danger[y][x - 1] > danger[y][x] + risk[y][x - 1]:
            danger[y][x - 1] = danger[y][x] + risk[y][x - 1]
            q.append((x - 1, y))
        if x < len(danger[y]) - 1 and \
           danger[y][x + 1] > danger[y][x] + risk[y][x + 1]:
            danger[y][x + 1] = danger[y][x] + risk[y][x + 1]
            q.append((x + 1, y))
        if y > 0 and danger[y - 1][x] > danger[y][x] + risk[y - 1][x]:
            danger[y - 1][x] = danger[y][x] + risk[y - 1][x]
            q.append((x, y - 1))
        if y < len(danger) - 1 and \
           danger[y + 1][x] > danger[y][x] + risk[y + 1][x]:
            danger[y + 1][x] = danger[y][x] + risk[y + 1][x]
            q.append((x, y + 1))

    print(danger[-1][-1])