def move_east(old_m):
    new_m = [['.' for x in line] for line in old_m]
    for i in range(len(old_m)):
        for j in range(len(old_m[i])):
            if old_m[i][j] == 'v':
                new_m[i][j] = 'v'
            elif old_m[i][j] == '>':
                if old_m[i][(j + 1) % len(old_m[i])] == '.':
                    new_m[i][(j + 1) % len(new_m[i])] = '>'
                else:
                    new_m[i][j] = '>'
    return new_m

def move_south(old_m):
    new_m = [['.' for x in line] for line in old_m]
    for i in range(len(old_m)):
        for j in range(len(old_m[i])):
            if old_m[i][j] == '>':
                new_m[i][j] = '>'
            elif old_m[i][j] == 'v':
                if old_m[(i + 1) % len(old_m)][j] == '.':
                    new_m[(i + 1) % len(old_m)][j] = 'v'
                else:
                    new_m[i][j] = 'v'
    return new_m
    # return old_m

with open('tests/25_1.input', 'r') as inp:
    old_m = [[x for x in line] for line in inp.read()[:-1].split('\n')]

    steps = 0
    while True:
        steps += 1
        new_m = move_east(old_m)
        new_m = move_south(new_m)
        if new_m == old_m:
            break

        old_m = new_m

    # for line in new_m:
    #     print(''.join(line))


    print(steps)