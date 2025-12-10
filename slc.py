class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def slc(graph, d, k):
    nodes = list(graph)
    uf = UnionFind(nodes)
    edges = list(graph.edges())
    edges.sort(key=d)
    clusters = len(nodes)

    for u, v in edges:
        if clusters == k:
            break
        if uf.union(u, v):
            clusters -= 1

    groups = {}
    for node in nodes:
        r = uf.find(node)
        groups.setdefault(r, set()).add(node)

    return frozenset(frozenset(g) for g in groups.values())
