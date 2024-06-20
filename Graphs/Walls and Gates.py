from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: 'List[List[int]]') -> None:
        if not grid:
            return None

        Rows = len(grid)
        Cols = len(grid[0])
        inf = 2147483647

        def bfs(r, c):
            visit = set()
            temp_q = deque()
            temp_q.append((r, c, 0))
            visit.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while temp_q:
                r, c, moves = temp_q.popleft()
                for i, j in directions:
                    new_r = r + i
                    new_c = c + j
                    if ((new_r, new_c) not in visit) and (new_r in range(Rows)) and (new_c in range(Cols)) and \
                            grid[new_r][new_c] != -1:
                        if grid[new_r][new_c] == 0:
                            return moves + 1
                        temp_q.append((new_r, new_c, moves + 1))
                        visit.add((new_r, new_c))

            return inf

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] != -1 and grid[r][c] != 0:
                    moves = bfs(r, c)
                    grid[r][c] = moves

