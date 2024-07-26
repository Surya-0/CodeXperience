import heapq
from collections import defaultdict

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        heap = []
        adj_list = defaultdict(list)
        for u, v, dist in edges:
            adj_list[u].append((v, dist))
            adj_list[v].append((u, dist))

        def dijkstra(node):
            heap = [(0, node)]  # dist,node
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                visit.add(node)
                for nei, dist2 in adj_list[node]:
                    if nei not in visit:
                        nei_dist = dist2 + dist
                        if nei_dist <= distanceThreshold:
                            heapq.heappush(heap, (nei_dist, nei))
                            # print(nei," ",nei_dist)
                            # visit.add(nei)
            # print("Visit set is : ",visit)
            return len(visit) - 1

        res = -1
        min_count = float('inf')
        for src in range(n):
            count = dijkstra(src)
            # print("Count is : ",count)
            if count <= min_count:
                res = src
                min_count = count

        return res
