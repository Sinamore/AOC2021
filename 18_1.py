class Tree:
    def __init__(self, lhs=None, rhs=None, value=None):
        self.lhs = lhs
        self.rhs = rhs
        self.value = value
        self.parent = None
        self.type = None
        if lhs:
            lhs.parent = self
        if rhs:
            rhs.parent = self

    def __str__(self):
        if self.value != None:
            return str(self.value)
        else:
            return '[' + str(self.lhs) + ',' + str(self.rhs) + ']'

def make_tree(stream):
    stack = []
    for tok in stream:
        if tok.isdigit():
            stack.append(Tree(None, None, int(tok)))
        elif tok == ']':
            top = stack.pop()
            top.type = 'R'
            nxt = stack.pop()
            nxt.type = 'L'
            t = Tree(nxt, top)
            # actually tree_add(nxt, top)
            stack.append(t)

    return stack.pop()

def tree_add(lhs, rhs):
    lhs.type = 'L'
    rhs.type = 'R'
    return Tree(lhs, rhs)

def tree_explode(t, h):
    res = False
    if h < 4:
        if t.lhs:
            res |= tree_explode(t.lhs, h + 1)
        if not res:
            if t.rhs:
                res |= tree_explode(t.rhs, h + 1)
    else: # h == 4
        if t.lhs and t.rhs:
            if t.lhs.value == None or t.rhs.value == None:
                print('Bad tree')
                exit()
            # up l
            tl = t
            while tl.parent and tl.type == 'L':
                tl = tl.parent
            if tl.parent:
                l = tl.parent.lhs
                while l.rhs:
                    l = l.rhs
                l.value = l.value + t.lhs.value
            # up r
            tr = t
            while tr.parent and tr.type == 'R':
                tr = tr.parent
            if tr.parent:
                r = tr.parent.rhs
                while r.lhs:
                    r = r.lhs
                r.value = r.value + t.rhs.value

            t.value = 0
            t.lhs = None
            t.rhs = None
            res = True
    return res

def tree_split(t):
    if t.value != None:
        if t.value > 9:
            lhs = Tree(None, None, t.value // 2)
            rhs = Tree(None, None, t.value - t.value // 2)
            if t.type == 'L':
                t.parent.lhs = tree_add(lhs, rhs)
                t.parent.lhs.type = 'L'
                t.parent.lhs.parent = t.parent
            else:
                t.parent.rhs = tree_add(lhs, rhs)
                t.parent.rhs.type = 'R'
                t.parent.rhs.parent = t.parent

            return True

    if t.lhs and tree_split(t.lhs):
        return True
    if t.rhs:
        return tree_split(t.rhs)
    return False

def tree_reduce(t):
    ok = True
    while ok:
        ok = False
        ok = tree_explode(t, 0)
        if not ok:
            ok = tree_split(t)
    return t

def tree_magnitude(t):
    if t.value != None:
        return t.value
    return tree_magnitude(t.lhs) * 3 + tree_magnitude(t.rhs) * 2


with open('tests/18_1.input', 'r') as inp:
    numbers = inp.read()[:-1].split('\n')
    n1 = make_tree(numbers[0])

    for n in numbers[1:]:
        n2 = make_tree(n)
        n1 = tree_add(n1, n2)
        n1 = tree_reduce(n1)

    print(n1)
    print(tree_magnitude(n1))