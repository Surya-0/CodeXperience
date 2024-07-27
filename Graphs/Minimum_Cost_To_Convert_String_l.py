from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = {}
        d = defaultdict(list)
        for i in range(len(original)):
            d[original[i]].append((changed[i], cost[i]))

        def bfs(src, target):
            temp = [(0, src)]
            visit = set()
            while temp:
                price, node = heapq.heappop(temp)
                if node == target:
                    return price
                visit.add(node)
                for nei, cost in d[node]:
                    if nei not in visit:
                        heapq.heappush(temp, (cost + price, nei))
            return -1

        res = 0
        for i in range(len(source)):
            if (source[i], target[i]) in dp:
                res += dp[(source[i], target[i])]
                continue

            val = bfs(source[i], target[i])

            if val == -1:
                return -1

            res += val
            dp[(source[i], target[i])] = val

        return res






