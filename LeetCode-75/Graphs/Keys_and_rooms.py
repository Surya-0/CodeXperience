from typing import List


class Solution:
    def __init__(self):
        self.adList = {}

    def add_node(self, node):
        self.adList[node] = []

    def add_edge(self, node1, node2):
        self.adList[node1].append(node2)

    def dfs(self, node):
        stack = [node]
        visit = set()
        res = []
        while stack:
            node = stack.pop()
            visit.add(node)
            res.append(node)
            for nei in self.adList[node]:
                if nei not in visit:
                    stack.append(nei)
                    visit.add(nei)

        return res

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        for i in range(n):
            self.add_node(i)

        for i, j in enumerate(rooms):
            for val in j:
                self.add_edge(i, val)

        res = self.dfs(0)

        return len(res) == n

