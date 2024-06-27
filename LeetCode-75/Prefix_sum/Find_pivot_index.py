class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        prefix_sum = [0] * len(nums)
        suffix_sum = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i + 1]

        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i

        return -1