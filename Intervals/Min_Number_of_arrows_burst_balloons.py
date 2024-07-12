from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = [points[0]]
        for start, end in points[1:]:
            if res[-1][1] >= start:
                res[-1][1] = min(res[-1][1], end)

            else:
                res.append([start, end])

        return len(res)
