from collections import defaultdict
class Graphs:

    def __init__(self):
        self.adj = defaultdict(list)
        self.visited = set()
        self.res_arr_dfs = []

    def add_edge(self,vertex1,vertex2):
        self.adj[vertex1].append(vertex2)
        self.adj[vertex2].append(vertex1)

    def print_adj_list(self):
        print(self.adj)

    def dfs(self,node):
        if node in self.visited:
            # print("Since ",node," is in visited we are backtracking")
            return

        self.visited.add(node)
        self.res_arr_dfs.append(node)
        neighbours = self.adj[node]
        for neighbor in neighbours:
            self.dfs(neighbor)

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
g.dfs(0)
print(g.res_arr_dfs)