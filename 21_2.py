rolls_n = 0
current = 0

def generate(scores):
    while True:
        n = dict()
        for p in scores[-1].keys():
            if p[0] <= 20:
                # sum_rolls = 3
                p3 = (p[1] + 3) % len(points)
                sc3 = p[0] + points[p3]
                if (sc3, p3) in n.keys():
                    n[(sc3, p3)] += scores[-1][p]
                else:
                    n[(sc3, p3)] = scores[-1][p]
                # sum_rolls = 4
                p4 = (p[1] + 4) % len(points)
                sc4 = p[0] + points[p4]
                if (sc4, p4) in n.keys():
                    n[(sc4, p4)] += 3 * scores[-1][p]
                else:
                    n[(sc4, p4)] = 3 * scores[-1][p]
                # sum_rolls = 5
                p5 = (p[1] + 5) % len(points)
                sc5 = p[0] + points[p5]
                if (sc5, p5) in n.keys():
                    n[(sc5, p5)] += 6 * scores[-1][p]
                else:
                    n[(sc5, p5)] = 6 * scores[-1][p]
                # sum_rolls = 6
                p6 = (p[1] + 6) % len(points)
                sc6 = p[0] + points[p6]
                if (sc6, p6) in n.keys():
                    n[(sc6, p6)] += 7 * scores[-1][p]
                else:
                    n[(sc6, p6)] = 7 * scores[-1][p]
                # sum_rolls = 7
                p7 = (p[1] + 7) % len(points)
                sc7 = p[0] + points[p7]
                if (sc7, p7) in n.keys():
                    n[(sc7, p7)] += 6 * scores[-1][p]
                else:
                    n[(sc7, p7)] = 6 * scores[-1][p]
                # sum_rolls = 8
                p8 = (p[1] + 8) % len(points)
                sc8 = p[0] + points[p8]
                if (sc8, p8) in n.keys():
                    n[(sc8, p8)] += 3 * scores[-1][p]
                else:
                    n[(sc8, p8)] = 3 * scores[-1][p]
                # sum_rolls = 9
                p9 = (p[1] + 9) % len(points)
                sc9 = p[0] + points[p9]
                if (sc9, p9) in n.keys():
                    n[(sc9, p9)] += scores[-1][p]
                else:
                    n[(sc9, p9)] = scores[-1][p]
        if len(n.keys()) == 0:
            return scores
        scores.append(n)


with open('tests/21_2.input', 'r') as inp:
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p1, p2 = [points.index(int(x.split(' ')[-1]))
                  for x in inp.read()[:-1].split('\n')]

    scores1 = [{(0, p1): 1}]
    scores2 = [{(0, p2): 1}]

    scores1 = generate(scores1)
    scores2 = generate(scores2)

    wins1, wins2 = 0, 0

    for turn in range(1, len(scores1)):
        results = scores1[turn]
        for key1 in results.keys():
            if key1[0] >= 21:
                result1 = results[key1]
                for key2 in scores2[turn - 1].keys():
                    if key2[0] < 21:
                        result2 = scores2[turn - 1][key2]
                        wins1 += (result1 * result2)

    for turn in range(len(scores2)):
        results = scores2[turn]
        for key2 in results.keys():
            if key2[0] >= 21:
                result2 = results[key2]
                for key1 in scores1[turn].keys():
                    if key1[0] < 21:
                        result1 = scores1[turn][key1]
                        wins2 += (result1 * result2)


    print(max(wins1, wins2))
