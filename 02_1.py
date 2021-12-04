with open('tests/02_1.input', 'r') as inp:
    x, depth = 0, 0
    for line in inp:
        direction, val = line.split()
        val = int(val)
        if direction == 'forward':
            x += val
        elif direction == 'up':
            depth -= val
        elif direction == 'down':
            depth += val

print(depth * x)