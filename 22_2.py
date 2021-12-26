import copy
from collections import deque

class Cuboid():
    def __init__(self, coords):
        self.xs = coords[0][0]
        self.xf = coords[0][1]
        self.ys = coords[1][0]
        self.yf = coords[1][1]
        self.zs = coords[2][0]
        self.zf = coords[2][1]

    def __str__(self):
        fmt = '[{}..{}] [{}..{}] [{}..{}]'
        return fmt.format(self.xs, self.xf, self.ys, self.yf, self.zs, self.zf)

    def intersects(self, other):
        if self.zf < other.zs:
            return False
        if other.zf < self.zs:
            return False
        if self.yf < other.ys:
            return False
        if other.yf < self.ys:
            return False
        if self.xf < other.xs:
            return False
        if other.xf < self.xs:
            return False
        return True

    def find_intersection(self, objects):
        for obj in objects:
            if self.intersects(obj[1]):
                return obj

        return None

with open('tests/22_2.input', 'r') as inp:
    commands = inp.read()[:-1].split('\n')
    for i in range(len(commands)):
        tmp = commands[i].split()
        tmp[1] = tmp[1].split(',')
        X = [int(x) for x in tmp[1][0][2:].split('..')]
        Y = [int(x) for x in tmp[1][1][2:].split('..')]
        Z = [int(x) for x in tmp[1][2][2:].split('..')]
        if X[0] > X[1] or Y[0] > Y[1] or Z[0] > Z[1]:
            print(commands[i])
        commands[i] = [tmp[0], Cuboid([X, Y, Z])]

    # objects do not intersect!
    # objects are switched-on cubes
    objects = []

    commands_d = deque(commands)

    while len(commands_d) > 0:

        obj1 = commands_d.popleft()
        if obj1[0] == 'off':
            # do while there is an intersection
            obj2 = obj1[1].find_intersection(objects)
            while obj2:
                objects.remove(obj2)
                if obj2[1].zs < obj1[1].zs:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].zf = obj1[1].zs - 1
                    objects.append(new_obj)
                    obj2[1].zs = obj1[1].zs

                if obj2[1].zf > obj1[1].zf:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].zs = obj1[1].zf + 1
                    objects.append(new_obj)
                    obj2[1].zf = obj1[1].zf

                if obj2[1].ys < obj1[1].ys:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].yf = obj1[1].ys - 1
                    objects.append(new_obj)
                    obj2[1].ys = obj1[1].ys

                if obj2[1].yf > obj1[1].yf:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].ys = obj1[1].yf + 1
                    objects.append(new_obj)
                    obj2[1].yf = obj1[1].yf

                if obj2[1].xs < obj1[1].xs:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].xf = obj1[1].xs - 1
                    objects.append(new_obj)
                    obj2[1].xs = obj1[1].xs

                if obj2[1].xf > obj1[1].xf:
                    new_obj = copy.deepcopy(obj2)
                    new_obj[1].xs = obj1[1].xf + 1
                    objects.append(new_obj)
                    obj2[1].xf = obj1[1].xf

                obj2 = obj1[1].find_intersection(objects)
        else:
            obj2 = obj1[1].find_intersection(objects)
            if not obj2:
                objects.append(obj1)
                continue

            # We need to split new obj (obj1) and put into commands_d 
            if obj1[1].zs < obj2[1].zs:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].zf = obj2[1].zs - 1
                commands_d.appendleft(new_obj)
                obj1[1].zs = obj2[1].zs

            if obj1[1].zf > obj2[1].zf:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].zs = obj2[1].zf + 1
                commands_d.appendleft(new_obj)
                obj1[1].zf = obj2[1].zf

            if obj1[1].ys < obj2[1].ys:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].yf = obj2[1].ys - 1
                commands_d.appendleft(new_obj)
                obj1[1].ys = obj2[1].ys

            if obj1[1].yf > obj2[1].yf:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].ys = obj2[1].yf + 1
                commands_d.appendleft(new_obj)
                obj1[1].yf = obj2[1].yf

            if obj1[1].xs < obj2[1].xs:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].xf = obj2[1].xs - 1
                commands_d.appendleft(new_obj)
                obj1[1].xs = obj2[1].xs

            if obj1[1].xf > obj2[1].xf:
                new_obj = copy.deepcopy(obj1)
                new_obj[1].xs = obj2[1].xf + 1
                commands_d.appendleft(new_obj)
                obj1[1].xf = obj2[1].xf

    print(sum((obj[1].xf - obj[1].xs + 1) *
              (obj[1].yf - obj[1].ys + 1) *
              (obj[1].zf - obj[1].zs + 1) for obj in objects))