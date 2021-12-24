class Beacon:
    def __init__(self, pos=tuple(), neigh=[]):
        self.pos = pos
        self.neighbours = set([(x[0] - pos[0],
                                x[1] - pos[1],
                                x[2] - pos[2]) for x in neigh if x != pos])

    def rotate(self, d, r):
        b = Beacon()
        b.pos = rotate(self.pos, d, r)
        b.neighbours = set([rotate(n, d, r) for n in self.neighbours])
        return b

D1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
D2 = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
D3 = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
D4 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
D5 = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
D6 = [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
D = [D1, D2, D3, D4, D5, D6]

R1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
R2 = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
R3 = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
R4 = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
R = [R1, R2, R3, R4]

# return a list of beacons
def rotate(pos, d, r):
    pos = (d[0][0] * pos[0] + d[0][1] * pos[1] + d[0][2] * pos[2],
           d[1][0] * pos[0] + d[1][1] * pos[1] + d[1][2] * pos[2],
           d[2][0] * pos[0] + d[2][1] * pos[1] + d[2][2] * pos[2])
    pos = (r[0][0] * pos[0] + r[0][1] * pos[1] + r[0][2] * pos[2],
           r[1][0] * pos[0] + r[1][1] * pos[1] + r[1][2] * pos[2],
           r[2][0] * pos[0] + r[2][1] * pos[1] + r[2][2] * pos[2])
    return pos

class Scanner:
    def __init__(self, beacons):
        self.pos = None
        self.rot = None
        self.beacon_sets = []
        b = [Beacon(x, beacons) for x in beacons]
        for d in D:
            for r in R:
                self.beacon_sets.append([x.rotate(d, r) for x in b])

def try_match(known_pos, unknown_pos, i, sc1, sc2):
    for i_b in range(len(sc2.beacon_sets)):
        beacon_set = sc2.beacon_sets[i_b]
        for b1 in sc1.beacon_sets[sc1.rot]:
            for b2 in beacon_set:
                if len(b1.neighbours & b2.neighbours) >= 11:
                    sc2.rot = i_b
                    sc2.pos = [sc1.pos[0] + b1.pos[0] - b2.pos[0],
                               sc1.pos[1] + b1.pos[1] - b2.pos[1],
                               sc1.pos[2] + b1.pos[2] - b2.pos[2]]
                    known_pos.append(sc2)
                    unknown_pos.pop(i)
                    return True
    return False

def manh(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])

with open('tests/19_2.input', 'r') as inp:
    scanners = inp.read()[:-1].split('\n\n')
    scanners = [x.split('\n')[1:] for x in scanners]

    for i in range(len(scanners)):
        scanners[i] = Scanner([tuple([int(y) for y in x.split(',')]) for x in scanners[i]])

    scanners[0].pos = [0, 0, 0]
    scanners[0].rot = 0

    known_pos = [scanners[0]]
    unknown_pos = scanners[1:]

    while len(unknown_pos) > 0:
        match = False
        for i in range(len(unknown_pos)):
            sc2 = unknown_pos[i]
            for j in range(len(known_pos)):
                sc1 = known_pos[j]
                # Try match
                if try_match(known_pos, unknown_pos, i, sc1, sc2):
                    match = True
                    break
            if match:
                break

    all_beacons = set()
    for sc in scanners:
        sc_set = set([(sc.pos[0] + x.pos[0],
                       sc.pos[1] + x.pos[1],
                       sc.pos[2] + x.pos[2]) for x in sc.beacon_sets[sc.rot]])
        all_beacons.update(sc_set)

    mx = 0
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            mx = max(mx, manh(scanners[i].pos, scanners[j].pos))

    print(mx)