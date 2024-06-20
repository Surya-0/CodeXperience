# Using dfs
class Solution1:

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



# Using Union find
class Solution2:

    def countComponents(self, n: int, edges: 'List[List[int]]') -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # This is for finding the parent
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1

        count = n
        for n1, n2 in edges:
            count -= union(n1, n2)

        return count

