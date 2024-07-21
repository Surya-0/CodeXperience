from collections import defaultdict

from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v, dist in roads:
            adj_list[u].append((v, dist))
            adj_list[v].append((u, dist))
        visit = set()
        self.res = float('inf')

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei, dist in adj_list[node]:
                self.res = min(dist, self.res)
                dfs(nei)
            return

        dfs(1)
        return self.res

