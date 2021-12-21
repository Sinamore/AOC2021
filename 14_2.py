def do_expand(pairs_dict, rules):
    res = dict()

    for rule in rules:
        p = (rule[0][0], rule[1])
        if p in res.keys():
            res[p] += pairs_dict.get((rule[0][0], rule[0][1]), 0)
        else:
            res[p] = pairs_dict.get((rule[0][0], rule[0][1]), 0)

        p = (rule[1], rule[0][1])
        if p in res.keys():
            res[p] += pairs_dict.get((rule[0][0], rule[0][1]), 0)
        else:
            res[p] = pairs_dict.get((rule[0][0], rule[0][1]), 0)

    return res

with open('tests/14_2.input', 'r') as inp:
    t, r = inp.read().split('\n\n')
    rules = [x.split(' -> ') for x in r[:-1].split('\n')]

    pairs_dict = dict()
    for i in range(len(t) - 1):
        if (t[i], t[i + 1]) in pairs_dict.keys():
            pairs_dict[(t[i], t[i + 1])] += 1
        else:
            pairs_dict[(t[i], t[i + 1])] = 1

    for step in range(40):
        pairs_dict = do_expand(pairs_dict, rules)

    freqs = dict()
    for pair in pairs_dict.keys():
        if pair[0] in freqs.keys():
            freqs[pair[0]] += pairs_dict[pair]
        else:
            freqs[pair[0]] = pairs_dict[pair]
        if pair[1] in freqs.keys():
            freqs[pair[1]] += pairs_dict[pair]
        else:
            freqs[pair[1]] = pairs_dict[pair]

    freqs_list = sorted([[x, (freqs[x] + 1)// 2] for x in freqs.keys()], key=lambda x: x[1])
    print(freqs_list[-1][1] - freqs_list[0][1])
