from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 0 - sea , 1 - land
        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit:
                visit.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    print(r, " ", c)
                    count += 1

                if grid[r][c] == 1 and (((r == 0) or (r == rows - 1)) or ((c == 0) or (c == cols - 1))) and (
                r, c) not in visit:
                    print("hi")
                    dfs(r, c)

        return count - len(visit)

