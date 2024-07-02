class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        l = 0
        r = 0
        temp_sum = 0
        res = max(nums)
        while r < len(nums):
            if temp_sum < 0:
                l = r
                temp_sum = 0

            temp_sum += nums[r]
            res = max(temp_sum, res)
            r += 1

        return res

