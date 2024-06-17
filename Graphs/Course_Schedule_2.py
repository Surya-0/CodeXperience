from collections import deque


# Using a deque reduces the popping time complexity to O(1) from O(n)
class Solution:
    def __init__(self):
        self.adList = {}

    def add_node(self, u):
        self.adList[u] = []

    def add_edge(self, u, v):
        self.adList[u].append(v)

    def detect_cycle(self):
        res = []
        in_degree = {}
        temp_q = deque()
        for key in self.adList:
            in_degree[key] = 0

        for u in self.adList:
            for v in self.adList[u]:
                in_degree[v] += 1

        for k, v in in_degree.items():
            if in_degree[k] == 0:
                temp_q.append(k)

        while temp_q:
            node = temp_q.popleft()
            res.append(node)
            for neighbour in self.adList[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    temp_q.append(neighbour)

        if len(res) == len(self.adList):
            return res

        else:
            return []

    def findOrder(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
        for i in range(numCourses):
            self.add_node(i)

        for i, j in prerequisites:
            self.add_edge(j, i)

        return self.detect_cycle()