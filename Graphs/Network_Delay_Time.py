from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We need to use Dijkstra's algorithm which uses BFS
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        visit = set()
        res = 0
        minheap = [(0, k)]  # time,node number
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue

            visit.add(n1)
            res = max(res, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 + w2, n2))  # This is where the difference with prims comes

        return res if len(visit) == n else -1
