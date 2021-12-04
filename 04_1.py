def form_board(b):
    return [[int(x) for x in line.split()] for line in b.split('\n')]

def move(board, draw):
    for line in board:
        line[:] = [x if x != draw else -1 for x in line]
        if sum(line) == -5:
            return True
    for i in range(5):
        if sum(line[i] for line in board) == -5:
            return True

    return False

def score(board):
    return sum(x if x >= 0 else 0 for line in board for x in line)

with open('tests/04_1.input', 'r') as inp:
    tmp = inp.read()[:-1].split('\n\n')
    draws = [int(x) for x in tmp[0].split(',')]
    boards = [form_board(b) for b in tmp[1:]]
    for draw in draws:
        for board in boards:
            win = move(board, draw)
            if win:
                print(score(board) * draw)
                exit()
