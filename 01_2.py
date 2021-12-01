with open('tests/01_2.input', 'r') as inp:
    prev_x1 = None
    prev_x2 = None
    prev_sum = None
    counter = 0
    for line in inp:
        x = int(line)
        if prev_x1 == None:
            prev_x1 = x
            continue
        if prev_x2 == None:
            prev_x2 = x
            continue
        new_sum = prev_x1 + prev_x2 + x
        if prev_sum == None:
            prev_sum = new_sum
        else:
            if new_sum > prev_sum:
                counter += 1
        prev_sum = new_sum
        prev_x1 = prev_x2
        prev_x2 = x

print(counter)