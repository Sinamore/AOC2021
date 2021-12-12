def calc_size(x, y):
    if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
        return 0
    if m[y][x] == 9:
        return 0
    m[y][x] = 9
    return calc_size(x - 1, y) + calc_size(x + 1, y) + calc_size(x, y - 1) + calc_size(x, y + 1) + 1

with open('tests/09_2.input', 'r') as inp:
    m = [[int(h) for h in line[:-1]] for line in inp]
    mx1, mx2, mx3 = 0, 0, 0
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
            s = calc_size(x, y)
            if s > mx1:
                mx3, mx2, mx1 = mx2, mx1, s
            elif s > mx2:
                mx2, mx3 = mx3, s
            elif s > mx3:
                mx3 = s
    print(mx1 * mx2 * mx3)