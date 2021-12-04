with open('tests/03_1.input', 'r') as inp:
    g, eps = '', ''
    freq = None
    for line in inp:
        line = line[:-1]
        if freq == None:
            freq = [[0, 0] for i in range(len(line))]
        for i in range(len(line)):
            freq[i][int(line[i])] += 1

    for f in freq:
        if f[0] > f[1]:
            g += '0'
            eps += '1'
        else:
            g += '1'
            eps += '0'
    g, eps = int(g, 2), int(eps, 2)
    print(g * eps)