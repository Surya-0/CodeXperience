class Solution:
    def minSubArrayLen(self, target: int, nums: 'List[int]') -> int:
        min_len = float('inf')
        l = 0
        r = 0
        sumer = nums[r]
        while r < len(nums):
            if sumer < target:
                r += 1
                if r < len(nums):
                    sumer += nums[r]
            else:
                length = r - l + 1
                min_len = min(length, min_len)
                sumer -= nums[l]
                l = l + 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len