from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return res