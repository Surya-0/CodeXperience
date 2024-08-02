from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = nums.count(1)
        if total == 0:
            return 0
        l = 0
        r = total - 1
        n = len(nums)
        nums = nums + nums
        sub_arr = nums[l:r + 1]
        count_0 = sub_arr.count(0)
        count_1 = sub_arr.count(1)
        min_res = float('inf')
        while r < n + total - 1:
            min_res = min(min_res, total - count_1)
            if nums[l] == 0:
                count_0 -= 1
            else:
                count_1 -= 1
            l += 1
            r += 1
            if r < n + total - 1:
                if nums[r] == 0:
                    count_0 += 1
                else:
                    count_1 += 1

        return min_res



