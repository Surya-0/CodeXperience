from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0

        while l < r:

            temp = nums[l] + nums[r]
            if temp < k:
                l = l + 1

            elif temp > k:
                r = r - 1

            else:
                res += 1
                l += 1
                r -= 1
        return res
