class WeightedDirectedGraph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return str(self.graph)

    # adds a node that can point to others
    def add_new_node(self, u):
        self.graph[u] = {}

    # adds new edge from u to v with weight 0
    def add_new_edge(self, u, v):
        self.graph[u][v] = 0

    # increments edge weight by 1
    def increment_edge_weight(self, u, v):
        if u not in self.graph:
            self.add_new_node(u)
        if v not in self.graph[u]:
            self.add_new_edge(u, v)
        self.graph[u][v] += 1

