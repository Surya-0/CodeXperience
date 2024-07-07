from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}  # To store the max length of square for each coordinate

        # if length is l area is l * l

        def ms(r, c):
            if r >= rows or c >= cols:
                return 0

            if (r, c) not in cache:
                down = ms(r + 1, c)
                right = ms(r, c + 1)
                diag = ms(r + 1, c + 1)

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        ms(0, 0)

        return max(cache.values()) ** 2