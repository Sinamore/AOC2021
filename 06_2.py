t_max = 256
table = [[None for t in range(256)] for t0 in range(9)]

def calc(t_fish, t):
    if t_fish + t >= t_max:
        return 1
    if table[t_fish][t] == None:
        table[t_fish][t] = calc(6, t + t_fish + 1) + calc(8, t + t_fish + 1)
    return table[t_fish][t]

with open('tests/06_2.input', 'r') as inp:
    state = [int(x) for x in inp.read()[:-1].split(',')]
    print(sum(calc(fish, 0) for fish in state))
