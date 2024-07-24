from collections import defaultdict

from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adlist = defaultdict(list)
        for u, v in adjacentPairs:
            adlist[u].append(v)
            adlist[v].append(u)
        for k, v in adlist.items():
            if len(v) == 1:
                start = k
                break
        stack = []
        # print(start)
        visit = set()
        res = []

        def dfs(vertex):
            stack.append(vertex)
            visit.add(vertex)
            while stack:
                node = stack.pop()
                res.append(node)
                for nei in adlist[node]:
                    if nei not in visit:
                        stack.append(nei)
                        visit.add(nei)

        dfs(start)
        return res


