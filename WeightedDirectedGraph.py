class WeightedDirectedGraph:
    def __init__(self):
        self.adj_matrix = {}

    def __repr__(self):
        return str(self.adj_matrix)

    # adds a node that can point to others
    def add_new_node(self, u):
        self.adj_matrix[u] = {}

    # adds new edge from u to v with weight 0
    def add_new_edge(self, u, v):
        self.adj_matrix[u][v] = 0

    # increments edge weight by 1
    def increment_edge_weight(self, u, v):
        if u not in self.adj_matrix:
            self.add_new_node(u)
        if v not in self.adj_matrix[u]:
            self.add_new_edge(u, v)
        self.adj_matrix[u][v] += 1

