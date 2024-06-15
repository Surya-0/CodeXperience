class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count_islands = 0
        queue = []
        visited = set()

        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if (((r_new) in range(rows)) and ((c_new) in range(cols)) and grid[r_new][c_new] == "1" and (
                    r_new, c_new) not in visited):
                        visited.add((r_new, c_new))
                        queue.append((r_new, c_new))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count_islands += 1

        return count_islands




