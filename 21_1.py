rolls_n = 0
current = 0

def roll3():
    global rolls_n, current
    rolls_n += 3
    res = 3 * current + 6 
    current = (current + 3) % 100
    return res

with open('tests/21_1.input', 'r') as inp:
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p1, p2 = [points.index(int(x.split(' ')[-1]))
                  for x in inp.read()[:-1].split('\n')]

    score1, score2 = 0, 0

    while True:
        r = roll3()
        p1 = (p1 + r) % len(points)
        score1 += points[p1]
        if score1 >= 1000:
            score_l = score2
            break
        r = roll3()
        p2 = (p2 + r) % len(points)
        score2 += points[p2]
        if score2 >= 1000:
            score_l = score1
            break

    print(score_l * rolls_n)
