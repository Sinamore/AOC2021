with open('tests/02_2.input', 'r') as inp:
    x, aim, depth = 0, 0, 0
    for line in inp:
        direction, val = line.split()
        val = int(val)
        if direction == 'forward':
            x += val
            depth += (aim * val)
        elif direction == 'up':
            aim -= val
        elif direction == 'down':
            aim += val

print(depth * x)