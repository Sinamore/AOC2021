with open('tests/05_2.input', 'r') as inp:
    lines = []
    max_x, max_y = 0, 0
    for line in inp:
        p1, p2 = line.split(' -> ')
        x1, y1 = p1.split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = p2.split(',')
        x2, y2 = int(x2), int(y2)
        lines.append([x1, y1, x2, y2])
        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)
    max_x, max_y = max_x + 1, max_y + 1
    field = [[0 for y in range(max_y)] for x in range(max_x)]
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                field[x1][y] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                field[x][y1] += 1
        else:
            if abs(x2 - x1) != abs(y2 - y1):
                # Not diagonal
                continue
            if x2 < x1:
                x1, y1, x2, y2 = x2, y2, x1, y1
            dy = 0
            for x in range(x1, x2 + 1):
                field[x][y1 + dy] += 1
                if y2 > y1:
                    dy += 1
                else:
                    dy -= 1

print(sum(1 for y in range(max_y) for x in range(max_x) if field[x][y] >= 2))