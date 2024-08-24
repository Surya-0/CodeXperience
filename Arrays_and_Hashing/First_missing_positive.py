from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) + 1
        arr = [0] * n
        for i in range(len(nums)):
            if nums[i] in range(n):
                arr[nums[i] - 1] = nums[i]

        for i in range(len(arr)):
            if arr[i] == 0:
                return i + 1


