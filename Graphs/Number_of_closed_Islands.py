from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return 0

            if grid[r][c] == 1 or (r, c) in visit:
                return 1

            visit.add((r, c))
            return min(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visit:
                    count += dfs(r, c)

        return count
