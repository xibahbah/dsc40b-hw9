
class DSF:
    def __init__(self, nodes):
        """Initialize disjoint set forest with each node in its own set"""
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, node):
        """Find the root of the set containing node (with path compression)"""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return False
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True
    
    def get_clusters(self):
        clusters = {}
        for node in self.parent:
            root = self.find(node)
            if root not in clusters:
                clusters[root] = []
            clusters[root].append(node)
        
        return frozenset(frozenset(cluster) for cluster in clusters.values())


def slc(graph, d, k):
    
    nodes = list(graph.nodes())
    edges = []
    for edge in graph.edges():
        u, v = edge
        distance = d(edge)
        edges.append((distance, u, v))
  
    edges.sort()
  
    dsf = DSF(nodes)
    n = len(nodes)
    edges_needed = n - k
    edges_added = 0
    
    for distance, u, v in edges:
        if edges_added >= edges_needed:
            break
        if dsf.union(u, v):
            edges_added += 1
    return dsf.get_clusters()
if __name__ == "__main__":
    import dsc40graph
    
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'd')]
    for edge in edges:
        g.add_edge(*edge)
    
    def d(edge):
        u, v = sorted(edge)
        return {
            ('a', 'b'): 1,
            ('a', 'c'): 4,
            ('b', 'd'): 3,
            ('c', 'd'): 2,
        }[(u, v)]
    
    result = slc(g, d, 2)
    print(result)
