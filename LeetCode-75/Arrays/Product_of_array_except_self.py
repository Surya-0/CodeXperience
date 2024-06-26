class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        # We can solve this prefix concept
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length
        prefix[0] = 1
        suffix[-1] = 1
        res = []
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(length - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(0, length):
            res.append(prefix[i] * suffix[i])

        return res