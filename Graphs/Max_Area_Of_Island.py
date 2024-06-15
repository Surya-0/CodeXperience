class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> int:
        max_area = 0
        if not grid:
            return max_area

        visit = set()
        Rows = len(grid)
        Cols = len(grid[0])
        queue = []

        def bfs(r,c):
            visit.add((r,c))
            queue.append((r,c))
            area = 1
            while queue:
                r,c = queue.pop(0)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r_new = r+dr
                    c_new = c + dc
                    if ((r_new in range(Rows)) and (c_new in range(Cols)) and grid[r_new][c_new] == 1 and (r_new,c_new) not in visit):
                        queue.append((r_new,c_new))
                        visit.add((r_new,c_new))
                        area+=1

            return area

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] not in visit and grid[r][c] == 1:
                    # print("hi")
                    area = bfs(r,c)
                    # print(area)
                    max_area = max(area,max_area)

        return max_area
