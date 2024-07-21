from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ptr = 0
        res = 0
        while ptr < len(nums):
            count = 0
            while ptr < len(nums) and nums[ptr] == 0:
                count += 1
                ptr += 1
                res += count

            ptr += 1

        return res
