from collections import defaultdict
class Graphs:

    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self,vertex1,vertex2):
        self.adj[vertex1].append(vertex2)
        self.adj[vertex2].append(vertex1)

    def print_adj_list(self):
        print(self.adj)


g = Graphs()
g.add_edge(0,1)
g.add_edge(0,9)
g.add_edge(1,8)
g.add_edge(9,8)
g.add_edge(8,7)
g.add_edge(7,10)
g.add_edge(10,11)
g.add_edge(7,11)
g.add_edge(7,6)
g.add_edge(7,3)
g.add_edge(6,5)
g.add_edge(5,3)
g.add_edge(3,2)
g.add_edge(3,4)
g.print_adj_list()

