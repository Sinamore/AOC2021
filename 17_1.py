with open('tests/17_1.input', 'r') as inp:
    X, Y = inp.read()[13:-1].split(', ')
    x1, x2 = [int(x) for x in X[2:].split('..')]
    y1, y2 = [int(y) for y in Y[2:].split('..')]
    if y1 < 0:
        y0 = abs(y1) - 1
        print((y0 * (y0 + 1)) // 2)
    else:
        print('This is adhoc solution, figure out y1 >= 0 case later')
