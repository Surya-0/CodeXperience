class Solution:
    def __init__(self):
        self.adList = {}

    def add_node(self, node):
        self.adList[node] = []

    def add_edge(self, node1, node2):
        self.adList[node1].append(node2)
        self.adList[node2].append(node1)

    def detect_cycle(self, node, n):
        stack = []
        visit = set()
        res = []
        stack.append((node, -1))
        visit.add(node)
        while stack:
            cur, prev = stack.pop()
            res.append(cur)
            for nei in self.adList[cur]:
                if nei != prev:
                    if nei in visit:
                        # print("Hi")
                        return False
                    stack.append((nei, cur))
                    visit.add(nei)
        return len(res) == n

    def validTree(self, n: int, edges: 'List[List[int]]') -> bool:
        if not edges:
            return True

        for i in range(n):
            self.add_node(i)

        for i, j in edges:
            self.add_edge(i, j)

        return self.detect_cycle(0, n)