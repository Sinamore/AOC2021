with open('tests/17_2.input', 'r') as inp:
    X, Y = inp.read()[13:-1].split(', ')
    x1, x2 = [int(x) for x in X[2:].split('..')]
    y1, y2 = [int(y) for y in Y[2:].split('..')]

    # assume 0 < x1 < x2 and 0 > y2 > y1 (other cases are similar)
    v = []
    for x in range(1, x2 + 1):
        for y in range(y1, -y1):
            x0, y0 = 0, 0
            vx, vy = x, y
            while True:
                x0 += vx
                y0 += vy
                vx = max(0, vx - 1)
                vy = vy - 1
                if x1 <= x0 and x0 <= x2 and y1 <= y0 and y0 <= y2:
                    v.append((x, y))
                    break
                if x0 > x2:
                    break
                if y0 < y1:
                    break
    print(len(v))
