from typing import List


class Solution:
    def __init__(self):
        self.adList_temp = {}
        self.adList = {}

    def add_node(self, node):
        self.adList_temp[node] = []
        self.adList[node] = set()

    def add_edge(self, node1, node2):
        self.adList_temp[node1].append(node2)
        self.adList_temp[node2].append(node1)
        self.adList[node1].add(node2)

    def dfs(self, node):
        stack = [node]
        visit = set()
        res = 0
        # print(stack," ",visit)
        while stack:
            node = stack.pop()
            # print(node," ",visit)
            visit.add(node)
            for nei in self.adList_temp[node]:
                if nei not in visit:
                    stack.append(nei)
                    visit.add(nei)
                    if nei in self.adList[node]:
                        res += 1
        return res

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        for i in range(n):
            self.add_node(i)

        for u, v in connections:
            self.add_edge(u, v)

        # print(self.adList," ",self.adList_temp)

        res = self.dfs(0)

        return res