def do_expand(temp, rules):
    res = []
    for i in range(len(temp) - 1):
        res.append(temp[i])
        for rule in rules:
            if temp[i] == rule[0][0] and temp[i + 1] == rule[0][1]:
                res.append(rule[1])
                break
    res.append(temp[-1])
    return res

with open('tests/14_1.input', 'r') as inp:
    t, r = inp.read().split('\n\n')
    temp = [sym for sym in t]
    rules = [x.split(' -> ') for x in r[:-1].split('\n')]

    for step in range(10):
        temp = do_expand(temp, rules)

    freqs = dict()
    for sym in temp:
        if sym in freqs.keys():
            freqs[sym] += 1
        else:
            freqs[sym] = 1

    freqs_list = sorted([[x, freqs[x]] for x in freqs.keys()], key=lambda x: x[1])
    print(freqs_list[-1][1] - freqs_list[0][1])