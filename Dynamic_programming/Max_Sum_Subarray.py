class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        l = 0
        r = 0
        max_res = max(nums)
        temp = 0
        while r < len(nums):
            if temp < 0:
                temp = 0
                l = r

            temp += nums[r]
            max_res = max(temp, max_res)
            r = r + 1

        return max_res

