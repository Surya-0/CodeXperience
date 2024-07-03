from collections import deque

from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        def bfs(r, c):
            queue = deque()  # We need to append in the format of coordinates , moves
            visit = set()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            visit.add((r, c))
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (new_r in range(rows) and new_c in range(cols) and maze[new_r][new_c] == '.'):
                    queue.append((new_r, new_c, 1))
                    visit.add((new_r, new_c))

            while queue:
                r, c, moves = queue.popleft()
                if r == rows - 1 or c == cols - 1 or r == 0 or c == 0:
                    return moves

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in visit and maze[new_r][
                        new_c] == '.'):
                        queue.append((new_r, new_c, moves + 1))
                        visit.add((new_r, new_c))

            return -1

        return bfs(entrance[0], entrance[1])



