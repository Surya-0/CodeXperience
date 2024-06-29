import heapq
import math
class Solution:
    def kClosest(self, points: 'List[List[int]]', k: int) -> 'List[List[int]]':
        dist = []
        index = 0
        for i, j in points:
            distance = math.sqrt(i * i + j * j)
            heapq.heappush(dist, [distance, index])
            index += 1

        res = []
        while len(res) < k:
            _, ind = heapq.heappop(dist)
            res.append(points[ind])

        return res
