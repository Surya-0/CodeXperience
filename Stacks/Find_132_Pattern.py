from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # It will store the [value,the left min]
        left_min = nums[0]
        for n in nums:
            while stack and n > stack[-1][0]:
                stack.pop()

            if stack and stack[-1][0] > n > stack[-1][1]:
                return True

            left_min = min(left_min, n)
            stack.append((n, left_min))

        return False