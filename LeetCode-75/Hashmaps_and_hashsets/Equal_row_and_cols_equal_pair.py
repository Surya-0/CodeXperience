from collections import defaultdict


class Solution:
    def equalPairs(self, grid: 'List[List[int]]') -> int:
        n = len(grid)
        row_hash = defaultdict(int)
        col_hash = defaultdict(int)
        for i in range(n):
            row_tuple = tuple(grid[i])
            row_hash[row_tuple] += 1

        for j in range(n):
            col_tuple = tuple(grid[i][j] for i in range(n))
            col_hash[col_tuple] += 1

        res = 0
        for pair in row_hash:
            if pair in col_hash:
                res += row_hash[pair] * col_hash[pair]
        return res