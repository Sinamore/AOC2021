import queue

def next_v(path):
    l = []
    for e in edges[path[-1]]:
        if e.islower() and e not in path or e.isupper():
            p = path + [e]
            l.append(p)
    return l

with open('tests/12_1.input', 'r') as inp:
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
    paths.put(['start'])
    full_paths = []
    while paths.qsize() > 0:
        path = paths.get()
        if path[-1] == 'end':
            full_paths.append(path)
            continue
        for p in next_v(path):
            paths.put(p)

    print(len(full_paths))
