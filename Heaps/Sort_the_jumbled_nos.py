import heapq

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []
        res = []
        mapper = {}
        for ind, val in enumerate(mapping):
            mapper[str(ind)] = str(val)

        # print(mapper)

        for ind, val in enumerate(nums):
            temp = ""
            for ch in str(val):
                temp += mapper[ch]
            mapped_nums.append((int(temp), ind))
        print(mapped_nums)
        heapq.heapify(mapped_nums)
        while mapped_nums:
            val, ind = heapq.heappop(mapped_nums)
            res.append(nums[ind])

        return res




