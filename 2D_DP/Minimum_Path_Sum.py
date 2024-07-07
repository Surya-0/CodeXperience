from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])

        def mps(r, c):
            # If out of bounds, return a large number (effectively infinity)
            if r >= m or c >= n:
                return float('inf')

            # If reached the bottom-right cell, return its value
            if r == m - 1 and c == n - 1:
                return grid[r][c]

            # If already computed, return the memoized result
            if (r, c) in memo:
                return memo[(r, c)]

            # Compute the value and memoize it
            memo[(r, c)] = grid[r][c] + min(mps(r + 1, c), mps(r, c + 1))

            return memo[(r, c)]

        return mps(0, 0)
