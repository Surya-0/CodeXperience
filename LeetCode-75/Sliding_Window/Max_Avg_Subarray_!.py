class Solution:
    def findMaxAverage(self, nums: 'List[int]', k: int) -> float:
        l = 0
        r = k
        max_sum = float('-inf')
        sumer = 0

        for i in range(0, k):
            sumer += nums[i]

        max_sum = sumer
        while r < len(nums):
            sumer -= nums[l]
            sumer += nums[r]
            r += 1
            l += 1
            max_sum = max(sumer, max_sum)

        return (max_sum / k)









