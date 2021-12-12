def do_update(flash_q, y, x):
    if not octs[y][x][1]:
        octs[y][x][0] += 1
    if octs[y][x][0] > 9:
        flash_q.append([y, x])

def do_flash(flash_q, y, x):
    if octs[y][x][1]:
        return

    if y > 0:
        if x > 0:
            do_update(flash_q, y - 1, x - 1)
        do_update(flash_q, y - 1, x)
        if x < len(octs[y - 1]) - 1:
            do_update(flash_q, y - 1, x + 1)

    if x > 0:
        do_update(flash_q, y, x - 1)
    if x < len(octs[y]) - 1:
        do_update(flash_q, y, x + 1)

    if y < len(octs) - 1:
        if x > 0:
            do_update(flash_q, y + 1, x - 1)
        do_update(flash_q, y + 1, x)
        if x < len(octs[y + 1]) - 1:
            do_update(flash_q, y + 1, x + 1)

    octs[y][x][0] = 0
    octs[y][x][1] = True

def do_clear():
    for y in range(len(octs)):
        for x in range(len(octs[y])):
            octs[y][x][1] = False    

def do_step():
    flash_q = []
    for y in range(len(octs)):
        for x in range(len(octs[0])):
            octs[y][x][0] += 1

    for y in range(len(octs)):
        for x in range(len(octs[0])):
            if octs[y][x][0] > 9:
                flash_q.append([y, x])

    idx = 0
    while True:
        if idx > len(flash_q) - 1:
            break
        y, x = flash_q[idx][0], flash_q[idx][1]
        do_flash(flash_q, y, x)
        idx += 1

    flashes = sum(sum(1 for x in row if x[1]) for row in octs)
    do_clear()
    return flashes

with open('tests/11_1.input', 'r') as inp:
    octs = [[[int(x), False] for x in line] for line in inp.read()[:-1].split('\n')]

    octs_size = sum(1 for row in octs for x in row)
    step = 0
    while True:
        step += 1
        flashes = do_step()
        if flashes == octs_size:
            print(step)
            break

