from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.adList = defaultdict(list)

    def add_edge(self, u, v, val):
        self.adList[u].append((v, val))
        inv = 1 / val
        self.adList[v].append((u, inv))

    def bfs(self, src, target):
        if src not in self.adList or target not in self.adList:
            return -1
        queue = deque()
        visit = set()
        queue.append([src, 1])
        visit.add(src)
        while queue:
            node, w = queue.popleft()
            if node == target:
                return w

            for neighbor, weight in self.adList[node]:
                if neighbor not in visit:
                    queue.append([neighbor, w * weight])
                    visit.add(neighbor)

        return -1

    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]', queries: 'List[List[str]]') -> 'List[float]':
        for i in range(len(equations)):
            self.add_edge(equations[i][0], equations[i][1], values[i])

        res = []
        for q in queries:
            val = self.bfs(q[0], q[1])
            res.append(val)

        return res