from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0  # Stores the min number of intervals
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end

            else:
                res += 1
                prevEnd = min(prevEnd, end)  # We need to remove the interval with a higher end value

        return res
