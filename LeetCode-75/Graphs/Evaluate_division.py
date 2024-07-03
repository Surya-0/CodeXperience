from collections import defaultdict, deque

from typing import List


class Solution:
    def __init__(self):
        self.adList = defaultdict(list)

    def add_edge(self, var1, var2, val):
        self.adList[var1].append((var2, val))
        self.adList[var2].append((var1, 1 / val))

    def bfs(self, var1, var2):
        if var1 not in self.adList or var2 not in self.adList:
            return -1

        queue = deque()
        visit = set()
        queue.append((var1, 1))
        while queue:
            node, val = queue.popleft()
            if node == var2:
                return val

            for nei, wt in self.adList[node]:
                if nei not in visit:
                    queue.append((nei, val * wt))
                    visit.add(nei)

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for i, eq in enumerate(equations):
            self.add_edge(eq[0], eq[1], values[i])

        res = []
        for i, j in queries:
            res.append(self.bfs(i, j))

        return res
