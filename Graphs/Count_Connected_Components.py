class Solution:

    def __init__(self):
        self.adList = {}
        self.visit = set()

    def add_node(self, node):
        self.adList[node] = []

    def add_edge(self, node1, node2):
        self.adList[node1].append(node2)
        self.adList[node2].append(node1)

    def dfs(self, node):
        stack = []
        stack.append(node)
        self.visit.add(node)
        while stack:
            node = stack.pop()
            for nei in self.adList[node]:
                if nei not in self.visit:
                    stack.append(nei)
                    self.visit.add(nei)

    def countComponents(self, n: int, edges: 'List[List[int]]') -> int:
        if not edges:
            return n

        for i in range(n):
            self.add_node(i)

        for i, j in edges:
            self.add_edge(i, j)

        count = 0
        for i in range(n):
            if i not in self.visit:
                count += 1
                self.dfs(i)

        return count

