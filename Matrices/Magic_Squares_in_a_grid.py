from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def magic_square(r, c):
            # We need to check if the value is distinct and between 1 to 9
            val_set = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in val_set or not (1 <= grid[i][j] <= 9):
                        return 0
                    val_set.add(grid[i][j])

            # We need to check if the values across the rows are 15
            for i in range(r, r + 3):
                if sum(grid[i][c:c + 3]) != 15:
                    return 0

            # We need to check if the values across the colums are 15
            for i in range(c, c + 3):
                if (grid[r][i] + grid[r + 1][i] + grid[r + 2][i]) != 15:
                    return 0

            # We need to check if the values across the diagonals are 15
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or grid[r][c + 2] + grid[r + 1][c + 1] +
                    grid[r + 2][c] != 15):
                return 0

            return 1

        for r in range(rows - 2):
            for c in range(cols - 2):
                res += magic_square(r, c)
        return res