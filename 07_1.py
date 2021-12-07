with open('tests/07_1.input', 'r') as inp:
    positions = [int(x) for x in inp.read()[:-1].split(',')]
    min_p = min(positions)
    positions = [p - min_p for p in positions]
    weights = [0 for x in range(min_p, max(positions) + 1)]
    for i in range(len(weights)):
        weights[i] = sum(abs(p - i) for p in positions)
    print(min(weights))
