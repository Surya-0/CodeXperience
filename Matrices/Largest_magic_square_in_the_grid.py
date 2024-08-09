from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_k = min(rows, cols)
        res = 1

        def magic_square(r, c, k):
            target = sum(grid[r][c:c + k])
            # Calculation of row_sum
            for i in range(r, r + k):
                row_sum = sum(grid[i][c:c + k])

                if row_sum != target:
                    return False

            # Calculation of col_sum
            for i in range(c, c + k):
                col_sum = 0
                for j in range(r, r + k):
                    col_sum += grid[j][i]

                if col_sum != target:
                    return False

            # Calculation of diagonal sums

            pos_diag = sum(grid[r + i][c + i] for i in range(k))
            neg_diag = sum(grid[r + i][c + k - 1 - i] for i in range(k))

            if pos_diag != target or neg_diag != target:
                return False
            return True

        for r in range(rows):
            for c in range(cols):
                for k in range(2, max_k + 1):
                    # if r == 1 and c == 1:
                    # print(r," ",c," ",k)
                    if (r + k) in range(rows + 1) and (c + k) in range(cols + 1):
                        if magic_square(r, c, k):
                            # print("hello")
                            res = max(res, k)
        return res