from collections import defaultdict


class Graphs:

    def __init__(self):
        self.adj = defaultdict(list)
        self.visited = set()
        self.res_arr_dfs = []
        self.queue = []
        self.stack = []
        self.visited_dfs = set()
        self.visited_bfs = set()
        self.res_arr_bfs = []
        self.res_arr_dfs_2 = []

    def add_edge(self, vertex1, vertex2):
        self.adj[vertex1].append(vertex2)
        self.adj[vertex2].append(vertex1)

    def print_adj_list(self):
        print(self.adj)

    # DFS using Recursion
    def dfs(self, node):
        if node in self.visited:
            # print("Since ",node," is in visited we are backtracking")
            return

        self.visited.add(node)
        self.res_arr_dfs.append(node)
        neighbours = self.adj[node]
        for neighbor in neighbours:
            self.dfs(neighbor)

    # DFS using iterative approach
    def dfs_using_stack(self, node):
        if node in self.visited_dfs:
            return
        self.stack.append(node)
        self.visited_dfs.add(node)

        while self.stack:
            main_node = self.stack.pop()
            self.res_arr_dfs_2.append(main_node)
            for neighbor in self.adj[main_node]:
                if neighbor not in self.visited_dfs:
                    self.visited_dfs.add(neighbor)
                    self.stack.append(neighbor)

    # BFS using iterative approach
    def bfs(self, node):
        if node in self.visited_bfs:
            return

        self.visited_bfs.add(node)
        self.queue.append(node)
        while self.queue:
            main_node = self.queue.pop(0)
            self.res_arr_bfs.append(main_node)
            for neighbor in self.adj[main_node]:
                if neighbor not in self.visited_bfs:
                    self.queue.append(neighbor)
                    self.visited_bfs.add(neighbor)


g = Graphs()
g.add_edge(0, 1)
g.add_edge(0, 9)
g.add_edge(1, 8)
g.add_edge(9, 8)
g.add_edge(8, 7)
g.add_edge(7, 10)
g.add_edge(10, 11)
g.add_edge(7, 11)
g.add_edge(7, 6)
g.add_edge(7, 3)
g.add_edge(6, 5)
g.add_edge(5, 3)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.print_adj_list()
g.dfs(0)
print("________________________________________")
print("DFS done using recursion")
print(g.res_arr_dfs)
print("________________________________________")
g.bfs(0)
print("BFS done using iterative approach(queue)")
print(g.res_arr_bfs)
print("________________________________________")
print("DFS done using iterative approach(stack)")
g.dfs_using_stack(0)
print(g.res_arr_dfs_2)
