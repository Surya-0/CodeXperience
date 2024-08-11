from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit_set, avoid_set=None):
            stack = [(r, c)]
            directions = [[1, 0], [0, 1]]  # Only down and right
            while stack:
                r, c = stack.pop()
                if r == rows - 1 and c == cols - 1:
                    return True
                visit_set.add((r, c))
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (
                            new_r, new_c) not in visit_set:
                        if avoid_set and (new_r, new_c) in avoid_set:
                            continue
                        stack.append((new_r, new_c))
            return False

        first_visit = set()
        if not dfs(0, 0, first_visit):
            return True

        second_visit = set()
        if dfs(0, 0, second_visit, first_visit):
            return False

        return True
