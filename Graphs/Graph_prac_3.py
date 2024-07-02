# Graph definition, DFS, BFS, topological sort
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.adList = defaultdict(list)

    def add_edge(self, node1,node2):
        self.adList[node1].append(node2)

    def dfs(self,node):
        stack = [node]
        visited = set()

        while stack:
            node = stack.pop()
            visited.add(node)
            print(node)
            for nei in self.adList[node]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

    def bfs(self,node):
        queue = deque()
        visited = set()
        queue.append(node)

        while queue:
            node = queue.popleft()
            visited.add(node)
            print(node)
            for nei in self.adList[node]:
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)

    def topological_sort(self):
        in_degree = defaultdict(int)
        topo_sort = []
        for key in self.adList:
            for val in self.adList[key]:
                in_degree[val] += 1
        queue = deque()
        print("In-degree is : ",in_degree)
        for key,val in in_degree.items():
            if val == 0:
                queue.append(key)

        while queue:
            node = queue.popleft()
            topo_sort.append(node)

            for nei in self.adList[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        if len(topo_sort) == len(self.adList):
            return topo_sort

        else:
            return "Graph has a cycle"






