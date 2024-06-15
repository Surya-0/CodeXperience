class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return -1
        Rows = len(grid)
        Cols = len(grid[0])
        # visit = set()
        queue = []
        time = 0
        fresh = 0

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            l = len(queue)
            for i in range(l):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if ((r_new in range(Rows)) and (c_new in range(Cols)) and grid[r_new][c_new] == 1):
                        grid[r_new][c_new] = 2
                        queue.append((r_new, c_new))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1







