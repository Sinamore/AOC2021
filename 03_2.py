def compute_freqs(binaries, l):
    freqs = [[0, 0] for i in range(l)]
    for b in binaries:
        for i in range(l):
            if b[i] == '1':
                freqs[i][1] += 1
            else:
                freqs[i][0] += 1
    return freqs

def find_ox(binaries, l):
    freqs = compute_freqs(binaries, l)
    ox = [x for x in binaries]
    for i in range(l):
        f = '1' if freqs[i][1] >= freqs[i][0] else '0'
        ox_1 = [x for x in ox if x[i] == f]
        if len(ox_1) == 1:
            return ox_1[0]
        elif len(ox_1) == 0:
            return ox[-1]
        ox = ox_1
        freqs = compute_freqs(ox, l)

def find_co(binaries, l):
    freqs = compute_freqs(binaries, l)
    co = [x for x in binaries]
    for i in range(l):
        f = '0' if freqs[i][1] >= freqs[i][0] else '1'
        co_1 = [x for x in co if x[i] == f]
        if len(co_1) == 1:
            return co_1[0]
        elif len(co_1) == 0:
            return co[-1]
        co = co_1
        freqs = compute_freqs(co, l)

with open('tests/03_2.input', 'r') as inp:
    g, eps = '', ''
    freq = None
    binaries = []
    for line in inp:
        binaries.append(line[:-1])

    ox = find_ox(binaries, len(binaries[0]))
    co = find_co(binaries, len(binaries[0]))


    print(int(ox, 2) * int(co, 2))