with open('tests/01_1.input', 'r') as inp:
    prev = None
    counter = 0
    for line in inp:
        x = int(line)
        if prev == None:
            prev = x
            continue
        if x > prev:
            counter += 1
        prev = x

print(counter)