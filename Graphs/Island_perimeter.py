from collections import deque


class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            temp_q = deque()
            temp_q.append((r, c))
            visit.add((r, c))
            perimeter = 0
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while temp_q:
                r, c = temp_q.popleft()
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if r_new in range(rows) and c_new in range(cols):
                        if grid[r_new][c_new] == 1 and (r_new, c_new) not in visit:
                            temp_q.append((r_new, c_new))
                            visit.add((r_new, c_new))
                        elif grid[r_new][c_new] == 0:
                            perimeter += 1
                    else:
                        # If it's out of bounds, it's a water edge
                        perimeter += 1

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res += bfs(r, c)

        return res

