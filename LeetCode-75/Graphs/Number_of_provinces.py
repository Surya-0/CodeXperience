from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        if not isConnected:
            return res

        n = len(isConnected)
        visit = set()

        def dfs(node):
            stack = [node]
            while stack:
                node = stack.pop()
                visit.add(node)
                for i in range(n):
                    if isConnected[node][i] and i not in visit:
                        stack.append(i)
                        visit.add(i)

        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res
