from dsc40graph import UndirectedGraph
from dsf import DisjointSetForest

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
        clusters_dict.setdefault(root, set()).add(node)

    clusters = frozenset(frozenset(nodes) for nodes in clusters_dict.values())
    return clusters
