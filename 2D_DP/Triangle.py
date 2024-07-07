from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle[-1]) + 1)  # length of bottom row + 1

        for row in range(len(triangle) - 1, -1, -1):
            # print(dp)
            for ind, val in enumerate(triangle[row]):
                dp[ind] = val + min(dp[ind], dp[ind + 1])  # Check the condition in the question

        # print(dp)
        return dp[0]