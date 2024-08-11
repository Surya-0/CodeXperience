from collections import deque

from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c, visit):
            temp = deque()
            temp.append((r, c))
            visit.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while temp:
                r, c = temp.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (
                    new_r, new_c) not in visit:
                        temp.append((new_r, new_c))
                        visit.add((new_r, new_c))

        def count_islands():
            visit = set()
            count = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in visit:
                        bfs(r, c, visit)
                        count += 1
            return count

        c = count_islands()
        if c != 1:
            print(c)
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                grid[r][c] = 0  # Changing a land into water
                if count_islands() != 1:
                    return 1
                grid[r][c] = 1  # Changing water back into land

        return 2
