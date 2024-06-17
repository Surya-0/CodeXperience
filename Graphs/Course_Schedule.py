class Solution:
    def __init__(self):
        self.adList = {}

    def add_edge(self, u, v):
        if u not in self.adList:
            self.adList[u] = []

        if v not in self.adList:
            self.adList[v] = []

        self.adList[u].append(v)

    def can_complete(self):
        in_degree = {}
        temp_q = []
        count = 0
        for key in self.adList:
            in_degree[key] = 0

        for u in self.adList:
            for v in self.adList[u]:
                in_degree[v] += 1

        for k, v in in_degree.items():
            if in_degree[k] == 0:
                temp_q.append(k)

        while temp_q:
            node = temp_q.pop(0)
            count += 1
            for neighbor in self.adList[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    temp_q.append(neighbor)

        return count == len(self.adList)

    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        if not prerequisites:
            return True

        for i, j in prerequisites:
            self.add_edge(j, i)

        return self.can_complete()


