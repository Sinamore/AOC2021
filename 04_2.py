def form_board(b):
    return [[[int(x) for x in line.split()] for line in b.split('\n')], False]

def move(board, draw):
    for line in board[0]:
        line[:] = [x if x != draw else -1 for x in line]
        if sum(line) == -5:
            return True
    for i in range(5):
        if sum(line[i] for line in board[0]) == -5:
            return True

    return False

def score(board):
    return sum(x if x >= 0 else 0 for line in board[0] for x in line)

with open('tests/04_2.input', 'r') as inp:
    tmp = inp.read()[:-1].split('\n\n')
    draws = [int(x) for x in tmp[0].split(',')]
    boards = [form_board(b) for b in tmp[1:]]
    for draw in draws:
        for board in boards:
            board[1] = move(board, draw)
        if len(boards) == 1 and board[1]:
            print(score(boards[0]) * draw)
            exit()

        boards = [b for b in boards if not b[1]]