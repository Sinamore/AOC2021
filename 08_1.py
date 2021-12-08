with open('tests/08_1.input', 'r') as inp:
    s = 0
    for line in inp:
        left, right = line.split(' | ')
        right_list = right[:-1].split(' ')
        s += sum(1 if len(x) in [2, 3, 4, 7] else 0 for x in right_list)
    print(s)
