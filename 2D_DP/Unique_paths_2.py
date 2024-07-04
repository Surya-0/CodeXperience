
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the start or end is blocked, there is no path
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        memo = {}

        def upwo(r, c):
            if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
                return 0

            if r == 0 and c == 0:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = upwo(r - 1, c) + upwo(r, c - 1)

            return memo[(r, c)]

        return upwo(m - 1, n - 1)

class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)  # number of rows
        n = len(obstacleGrid[0])  # number of cols
        dp = [0] * n  # initialise an entire row of zeroes which is of length column
        dp[n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0

                elif c + 1 < n:
                    # We are doing this in place
                    dp[c] = dp[c] + dp[c + 1]

                else:
                    dp[c] = dp[c] + 0

        return dp[0]