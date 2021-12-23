sum_v = 0

def parse_literal(literal):
    parsed_sz = 0
    while True:
        parsed_sz += 5
        if literal[0] == '0':
            return parsed_sz
        literal = literal[5:]

# decode:
#  - literal
#    => parse_literal
#  - tl
#    => decode(substr)
#  - tn
#    => for i in range(n): decode()

def decode_package(bits, maxl=None, maxn=None):
    global sum_v
    v = int(bits[:3], 2)
    sum_v += v
    tid = int(bits[3:6], 2)
    if tid == 4:
        sz = parse_literal(bits[6:])
        return 6 + sz
    else:
        i = bits[6]
        if i == '0':
            tl = int(bits[7:22], 2)
            td = 0
            while td < tl:
                td += decode_package(bits[22 + td:])
            if td != tl:
                print('td {} != tl {}'.format(td, tl))
            return 22 + td
        else:
            tn = int(bits[7:18], 2)
            td = 0
            for i in range(tn):
                td += decode_package(bits[18 + td:])
            return 18 + td

with open('tests/16_1.input', 'r') as inp:
    res = []
    for sym in inp.read()[:-1]:
        res.append('{:04b}'.format(int(sym, 16)))
    bits = ''.join(res)
    decode_package(bits)
    print(sum_v)