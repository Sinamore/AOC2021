with open('tests/09_1.input', 'r') as inp:
    m = [[int(h) for h in line[:-1]] for line in inp]
    s = 0
    for y in range(len(m)):
        for x in range(len(m[0])):
            if y > 0 and m[y][x] >= m[y - 1][x]:
                continue
            if y < len(m) - 1 and m[y][x] >= m[y + 1][x]:
                continue
            if x > 0 and m[y][x] >= m[y][x - 1]:
                continue
            if x < len(m[y]) - 1 and m[y][x] >= m[y][x + 1]:
                continue
            s += m[y][x] + 1
    print(s)