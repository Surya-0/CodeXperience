from collections import defaultdict
class Graph_builder:
    def __init__(self):
        self.adList = defaultdict(list)
        self.visit_dfs = set()
        self.stack_dfs = []
        self.res_dfs = []
        self.res_bfs = []
        self.queue_bfs = []
        self.visit_bfs = set()

    def add_edge(self,node1,node2):
        self.adList[node1].append(node2)

    def dfs(self,node):
        if node in self.visit_dfs:
            return

        self.stack_dfs.append(node)
        self.visit_dfs.add(node)

        while self.stack_dfs:
            main_node = self.stack_dfs.pop()
            self.res_dfs.append(main_node)
            for neighbor in self.adList[main_node]:
                if neighbor not in self.visit_dfs:
                    self.stack_dfs.append(neighbor)
                    self.visit_dfs.add(neighbor)

    def bfs(self,node):
        if node in self.visit_bfs:
            return

        self.queue_bfs.append(node)
        self.visit_bfs.add(node)

        while self.queue_bfs:
            main_node = self.queue_bfs.pop(0)
            self.res_bfs.append(main_node)
            for neighbor in self.adList[main_node]:
                if neighbor not in self.visit_bfs:
                    self.queue_bfs.append(neighbor)
                    self.visit_bfs.add(neighbor)

    def topological_sort(self,node):
        in_degree = {}
        topo_sort = []
        for key in self.adList:
            in_degree[key] = 0

        for u in self.adList:
            for i in self.adList[u]:
                in_degree[i] += 1
        # print("The in-degree is : ",in_degree)
        temp_queue = []
        for key,val in in_degree.items():
            if in_degree[key] == 0:
                temp_queue.append(key)
        # print(temp_queue)
        while temp_queue:
            node = temp_queue.pop(0)
            topo_sort.append(node)

            for neighbour in self.adList[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    temp_queue.append(neighbour)

        if len(topo_sort) == len(self.adList):
            return topo_sort
        else:
            return "The graph contains a cycle"



g = Graph_builder()
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(4,5)
# g.add_edge(5,2)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,5)

g.dfs(1)
g.bfs(1)
topo = g.topological_sort(1)
print("The adjacency list is :",g.adList)
print("The dfs is : ",g.res_dfs)
print("The bfs is : ",g.res_bfs)
print("The topological order is : ",topo)


