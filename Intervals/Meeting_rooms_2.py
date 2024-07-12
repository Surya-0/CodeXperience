# Definition of Interval:
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        s = 0  # start array pointer
        e = 0  # end array pointer
        count = 0  # To measure the number of ongoing meetings

        res = 0  # To store the maximum number of concurrent meetings

        # print(start," ",end)
        while s < n:
            if start[s] < end[e]:
                count += 1
                s += 1

            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res


