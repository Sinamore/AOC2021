def do_fold(dots, fold):
    folded = set()
    if fold[0] == 'x':
        for dot in dots:
            if dot[0] <= fold[1]:
                folded.add(dot)
            else:
                folded.add((fold[1] - (dot[0] - fold[1]), dot[1]))
    elif fold[0] == 'y':
        for dot in dots:
            if dot[1] <= fold[1]:
                folded.add(dot)
            else:
                folded.add((dot[0], fold[1] - (dot[1] - fold[1])))
    return folded

with open('tests/13_1.input', 'r') as inp:
    d, f = inp.read().split('\n\n')
    dots = set(tuple([int(y) for y in x.split(',')]) for x in d.split('\n'))
    folds = [x.split('=') for x in f[:-1].split('\n')]
    folds = [[x[0][-1], int(x[1])] for x in folds]
    dots = do_fold(dots, folds[0])
    print(len(dots))