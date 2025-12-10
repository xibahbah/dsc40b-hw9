def slc(graph, d, k):

    nodes = list(graph)
    uf = UnionFind(nodes)
    num_clusters = len(nodes)
    edges = list(graph.edges())
    edges.sort(key=d)
    for u, v in edges:
        if num_clusters == k:
            break
        if uf.union(u, v):
            num_clusters -= 1
    clusters = {}
    for node in nodes:
        root = uf.find(node)
        clusters.setdefault(root, set()).add(node)
    return frozenset(frozenset(cluster) for cluster in clusters.values())
