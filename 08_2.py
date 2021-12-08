#  AAAA
# B    C
# B    C
#  DDDD
# E    F
# E    F
#  GGGG

# We need x -> X mapping
def get_set(l):
    if len(l) > 1:
        print('Error')
        exit()
    elif len(l) == 1:
        return l[0]
    else:
        return None

# def find_A(one, seven):
#     if not one or not seven:
#         print('find_A: not found')
#         return
#     a = [x for x in (seven - one)][0]
#     x_to_X[a] = 'A'
#     X_to_x['A'] = a

def find_B(three, four):
    if not three or not four:
        print('find_B: not found')
        return
    b = [x for x in (four - three)][0]
    x_to_X[b] = 'B'
    X_to_x['B'] = b

def find_C_and_F(one, len_6):
    if not one or not len_6:
        print('find_C_and_F: not found')
        return
    for i in len_6:
        if len(one - i) == 1:
            c = [x for x in (one - i)][0]
            x_to_X[c] = 'C'
            X_to_x['C'] = c
            f = [x for x in (one & i)][0]
            x_to_X[f] = 'F'
            X_to_x['F'] = f

# def find_D(zero, eight):
#     if not zero or not eight:
#         print('find_D: not found')
#         return
#     d = [x for x in (eight - zero)][0]
#     x_to_X[d] = 'D'
#     X_to_x['D'] = d

def find_E(two, three):
    if not two or not three:
        print('find_E: not found')
        return
    e = [x for x in (two - three)][0]
    x_to_X[e] = 'E'
    X_to_x['E'] = e

# def find_G():
#     g = [x for x in set(x_to_X.keys()) - set(X_to_x[k] for k in X_to_x.keys())][0]
#     x_to_X[g] = 'G'
#     X_to_x['G'] = g

with open('tests/08_2.input', 'r') as inp:
    s = 0
    for line in inp:
        l, r = line[:-1].split(' | ')
        left  = [set([sym for sym in x]) for x in l.split(' ')]
        right = [set([sym for sym in x]) for x in r.split(' ')]
        # Each line is independent
        x_to_X = dict()
        for sym in 'abcdefg':
            x_to_X[sym] = None
        X_to_x = dict()
        for sym in 'ABCDEFG':
            X_to_x[sym] = None
        one = [x for x in left if len(x) == 2]
        one = get_set(one)
        four = [x for x in left if len(x) == 4]
        four = get_set(four)
        seven = [x for x in left if len(x) == 3]
        seven = get_set(seven)
        eight = [x for x in left if len(x) == 7]
        eight = get_set(eight)

        # find_A(one, seven)

        len_6 = [x for x in left if len(x) == 6]
        find_C_and_F(one, len_6)

        len_5 = [x for x in left if len(x) == 5]
        three = [x for x in len_5 if X_to_x['C'] in x and X_to_x['F'] in x]
        three = get_set(three)

        find_B(three, four)

        five = [x for x in len_5 if X_to_x['B'] in x]
        five = get_set(five)

        two = [x for x in len_5 if not X_to_x['F'] in x]
        two = get_set(two)

        find_E(two, three)

        nine = [x for x in len_6 if not X_to_x['E'] in x]
        nine = get_set(nine)

        six = [x for x in len_6 if X_to_x['E'] in x and not X_to_x['C'] in x]
        six = get_set(six)

        zero = [x for x in len_6 if X_to_x['E'] in x and X_to_x['C'] in x]
        zero = get_set(zero)

        # find_D(zero, eight)

        # find_G()

        numbers = {
            ''.join(sorted([x for x in zero])): '0',
            ''.join(sorted([x for x in one])): '1',
            ''.join(sorted([x for x in two])): '2',
            ''.join(sorted([x for x in three])): '3',
            ''.join(sorted([x for x in four])): '4',
            ''.join(sorted([x for x in five])): '5',
            ''.join(sorted([x for x in six])): '6',
            ''.join(sorted([x for x in seven])): '7',
            ''.join(sorted([x for x in eight])): '8',
            ''.join(sorted([x for x in nine])): '9'
        }

        s += int(''.join([numbers[''.join(sorted([x for x in digit]))] for digit in right]))

    print(s)
