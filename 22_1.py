with open('tests/22_1.input', 'r') as inp:
    commands = inp.read()[:-1].split('\n')
    for i in range(len(commands)):
        tmp = commands[i].split()
        tmp[1] = tmp[1].split(',')
        X = [int(x) for x in tmp[1][0][2:].split('..')]
        Y = [int(x) for x in tmp[1][1][2:].split('..')]
        Z = [int(x) for x in tmp[1][2][2:].split('..')]
        if X[0] > X[1] or Y[0] > Y[1] or Z[0] > Z[1]:
            print(commands[i])
        commands[i] = [tmp[0], X, Y, Z]

    xs, xf = -50, 50
    ys, yf = -50, 50
    zs, zf = -50, 50

    space = [[[0 for x in range(xs, xf + 1)] for y in range(ys, yf + 1)]
             for z in range(zs, zf + 1)]

    v = {'off': 0, 'on': 1}

    for c in commands:
        if c[1][0] > xf or c[1][1] < xs or \
           c[2][0] > yf or c[2][1] < ys or \
           c[3][0] > zf or c[3][1] < zs:
            continue
        for z in range(max(c[3][0], zs), min(c[3][1], zf) + 1):
            for y in range(max(c[2][0], ys), min(c[2][1], yf) + 1):
                for x in range(max(c[1][0], xs), min(c[1][1], xf) + 1):
                    space[zs + z][ys + y][xs + x] = v[c[0]]


    print(sum(space[z][y][x] for z in range(len(space))
                             for y in range(len(space[z]))
                             for x in range(len(space[z][y]))))