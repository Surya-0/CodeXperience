from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag = 0
        for ind, val in enumerate(intervals):
            if val[0] > newInterval[0]:
                intervals.insert(ind, newInterval)
                flag = 1
                break

        if flag == 0:
            intervals.append(newInterval)

        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])

            else:
                res.append([start, end])

        return res




