class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        pre = 1
        post = 1

        # Prefix computation
        for i in range(0, len(nums)):
            res[i] = pre
            pre = nums[i] * pre

        # Postfix computation
        for i in range(-1, -len(nums) - 1, -1):
            res[i] *= post
            post = nums[i] * post

        return res
