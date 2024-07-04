class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        memo[(1, 1)] = 1

        def up(m, n):
            if (m, n) in memo:
                return memo[(m, n)]

            if m == 0 or n == 0:
                return 0

            if m == 1 or n == 1:
                return 1

            memo[(m, n)] = up(m - 1, n) + up(m, n - 1)

            return memo[(m, n)]

        return up(m, n)

