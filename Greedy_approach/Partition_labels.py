from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind = {}
        for i, v in enumerate(s):
            lastind[v] = i

        res = []
        size = 0
        end = 0
        for i, v in enumerate(s):
            size += 1
            # if lastind[v] > end:
            #     end = lastind[v]
            end = max(end, lastind[v])
            if i == end:
                res.append(size)
                size = 0

        return res