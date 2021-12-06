def step(state):
    l = len(state)
    for i in range(l):
        if state[i] == 0:
            state[i] = 6
            state.append(8)
        else:
            state[i] -= 1

with open('tests/06_1.input', 'r') as inp:
    state = [int(x) for x in inp.read()[:-1].split(',')]
    for i in range(80):
        step(state)
    print(len(state))