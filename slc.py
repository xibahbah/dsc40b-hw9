class DisjointSetForest:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


def slc(graph, d, k):
    dsf = DisjointSetForest()
    for node in graph.nodes:
        dsf.make_set(node)

    edges = []
    for u, v in graph.edges:
        w = d((u, v))
        edges.append((w, u, v))

    edges.sort(key=lambda x: x[0])

    num_clusters = len(graph.nodes)

    for w, u, v in edges:
        if num_clusters <= k:
            break
        if dsf.find(u) != dsf.find(v):
            dsf.union(u, v)
            num_clusters -= 1

    clusters_dict = {}
    for node in graph.nodes:
        root = dsf.find(node)
        if root not in clusters_dict:
            clusters_dict[root] = set()
        clusters_dict[root].add(node)

    clusters = frozenset(frozenset(nodes) for nodes in clusters_dict.values())
    return clusters
