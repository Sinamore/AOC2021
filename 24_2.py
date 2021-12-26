from collections import deque
import itertools
from math import inf

class VM:
    def __init__(self):
        self.regs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def __str__(self):
        fmt = 'VM: w = {}, x = {}, y = {}, z = {}, input: [{}]'
        return fmt.format(hex(self.regs['w']),
                          hex(self.regs['x']),
                          hex(self.regs['y']),
                          hex(self.regs['z']),
                          ' '.join(str(x) for x in self.input)
                              if hasattr(self, 'input') else None)

    def reset(self):
        self.regs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def execute(self, prog, input_stream):
        self.input = deque(input_stream)
        for cmd in prog:
            self.execute_cmd(cmd)

        z = self.regs['z']
        vm.reset()
        return z

    def execute_z(self, prog, x, z):
        self.input = deque([x])
        self.regs['z'] = z
        for cmd in prog:
            self.execute_cmd(cmd)

        z = self.regs['z']
        vm.reset()
        return z


    def execute_cmd(self, cmd):
        cmd = cmd.split(' ')
        if cmd[0] == 'inp':
            self.execute_inp(cmd[1])
        else:
            try:
                cmd[2] = int(cmd[2])
            except:
                pass
            if cmd[0] == 'add':
                self.execute_add(cmd[1], cmd[2])
            elif cmd[0] == 'mul':
                self.execute_mul(cmd[1], cmd[2])
            elif cmd[0] == 'div':
                self.execute_div(cmd[1], cmd[2])
            elif cmd[0] == 'mod':
                self.execute_mod(cmd[1], cmd[2])
            elif cmd[0] == 'eql':
                self.execute_eql(cmd[1], cmd[2])
            else:
                print('Unknown cmd: {}', cmd[0])
                exit()

    def execute_inp(self, reg):
        self.regs[reg] = self.input.popleft()

    def execute_add(self, lhs, rhs):
        if isinstance(rhs, int):
            self.regs[lhs] = self.regs[lhs] + rhs
        else:
            self.regs[lhs] = self.regs[lhs] + self.regs[rhs]

    def execute_mul(self, lhs, rhs):
        if isinstance(rhs, int):
            self.regs[lhs] = self.regs[lhs] * rhs
        else:
            self.regs[lhs] = self.regs[lhs] * self.regs[rhs]

    def execute_div(self, lhs, rhs):
        if isinstance(rhs, int):
            self.regs[lhs] = self.regs[lhs] // rhs
        else:
            self.regs[lhs] = self.regs[lhs] // self.regs[rhs]

    def execute_mod(self, lhs, rhs):
        if isinstance(rhs, int):
            self.regs[lhs] = self.regs[lhs] % rhs
        else:
            self.regs[lhs] = self.regs[lhs] % self.regs[rhs]

    def execute_eql(self, lhs, rhs):
        if isinstance(rhs, int):
            self.regs[lhs] = 1 if self.regs[lhs] == rhs else 0
        else:
            self.regs[lhs] = 1 if self.regs[lhs] == self.regs[rhs] else 0


with open('tests/24_1.input', 'r') as inp:
    lines = inp.read()[:-1].split('\n')
    subp = []
    rt = []
    for line in lines:
        if line.startswith('inp'):
            if len(rt) > 0:
                subp.append(tuple(rt))
            rt = [line]
        else:
            rt.append(line)
    if len(rt) > 0:
        subp.append(tuple(rt))

    subp[0] = ('inp w', 'add z 7', 'add z w')
    subp[1] = ('inp w', 'mul z 26', 'add z 4', 'add z w')
    subp[2] = ('inp w', 'mul z 26', 'add z 8', 'add z w')

    subp[4] = ('inp w', 'mul z 26', 'add z 5', 'add z w')
    subp[5] = ('inp w', 'mul z 26', 'add z 14', 'add z w')
    subp[6] = ('inp w', 'mul z 26', 'add z 12', 'add z w')

    subp[9] = ('inp w', 'mul z 26', 'add z 7', 'add z w')

    print([9**x for x in range(10)])
    res = set()
    vm = VM()
    z_dict = {0: 0}
    for i in range(14):
        n_dict = dict()
        for z in z_dict.keys():
            for w in range(1, 10):
                res1 = vm.execute_z(subp[i], w, z)
                n_dict[res1] = min(n_dict.get(res1, inf), z_dict[z] * 10 + w)
        z_dict = n_dict
        print(len(z_dict.keys()))

    print(z_dict[0])