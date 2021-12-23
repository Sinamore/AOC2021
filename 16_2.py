def parse_literal(literal):
    parsed_sz, value = 0, ''
    while True:
        parsed_sz += 5
        value += literal[1:5]
        if literal[0] == '0':
            return [parsed_sz, int(value, 2)]
        literal = literal[5:]

def op(opcode, values):
    if opcode == 0:
        return sum(values)
    elif opcode == 1:
        p = 1
        for i in values:
            p *= i
        return p
    elif opcode == 2:
        return min(values)
    elif opcode == 3:
        return max(values)
    elif opcode == 5:
        return 1 if (values[0] > values[1]) else 0
    elif opcode == 6:
        return 1 if (values[0] < values[1]) else 0
    elif opcode == 7:
        return 1 if (values[0] == values[1]) else 0
    else:
        print('Unknown opcode', opcode)

# decode:
#  - literal
#    => parse_literal
#  - tl
#    => decode(substr)
#  - tn
#    => for i in range(n): decode()

def decode_package(bits, maxl=None, maxn=None):
    v = int(bits[:3], 2)
    tid = int(bits[3:6], 2)
    if tid == 4:
        sz, val = parse_literal(bits[6:])
        return [6 + sz, val]
    else:
        i = bits[6]
        vals = []
        if i == '0':
            tl = int(bits[7:22], 2)
            td = 0
            while td < tl:
                res = decode_package(bits[22 + td:])
                td += res[0]
                vals.extend(res[1:])
            if td != tl:
                print('td {} != tl {}'.format(td, tl))
            return [22 + td, op(tid, vals)]
        else:
            tn = int(bits[7:18], 2)
            td = 0
            for i in range(tn):
                res = decode_package(bits[18 + td:])
                td += res[0]
                vals.extend(res[1:])
            return [18 + td, op(tid, vals)]

with open('tests/16_2.input', 'r') as inp:
    res = []
    for sym in inp.read()[:-1]:
        res.append('{:04b}'.format(int(sym, 16)))
    bits = ''.join(res)
    print(decode_package(bits)[1])
