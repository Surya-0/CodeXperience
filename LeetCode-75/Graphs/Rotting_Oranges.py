from collections import deque

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visit = set()
        num_fresh = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))

                elif grid[i][j] == 1:
                    num_fresh += 1

        while queue and num_fresh:
            len_q = len(queue)
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for i in range(len_q):
                r, c = queue.popleft()
                visit.add((r, c))
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in visit and grid[new_r][
                        new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        visit.add((new_r, new_c))
                        num_fresh -= 1

            time += 1

        return time if num_fresh == 0 else -1

