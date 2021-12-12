import queue

def next_v(path):
    l = []
    for e in edges[path[0][-1]]:
        if e == 'start':
            continue
        if e.islower() and (e not in path[0] or not path[1]) or e.isupper():
            p = path[0] + [e]
            if e.islower() and e in path[0]:
                l.append([p, True])
            else:
                l.append([p, path[1]])
    return l

with open('tests/12_2.input', 'r') as inp:
    edges = dict()
    for line in inp:
        b,e = line[:-1].split('-')
        if not b in edges.keys():
            edges[b] = {e}
        else:
            edges[b].add(e)
        if not e in edges.keys():
            edges[e] = {b}
        else:
            edges[e].add(b)
    paths = queue.Queue()
    paths.put([['start'], False])
    full_paths = []
    while paths.qsize() > 0:
        path = paths.get()
        if path[0][-1] == 'end':
            full_paths.append(path)
            continue
        for p in next_v(path):
            paths.put(p)

    print(len(full_paths))
