from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i: [] for i in range(n)}  # i : list of [cost,point]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algo
        res = 0  # cost
        visit = set()
        minheap = [[0, 0]]  # cost,point
        while len(visit) < n:
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neicost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap, [neicost, nei])

        return res