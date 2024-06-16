class Solution:
    def pacificAtlantic(self, heights: 'List[List[int]]') -> 'List[List[int]]':
        Rows = len(heights)
        Cols = len(heights[0])
        # visit = set()
        # stack = []
        res = []
        if not heights:
            return res

        def dfs(r, c):
            stack = [(r, c)]
            visit = {(r, c)}
            temp = [0, 0]
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    if ((r + dr) < 0 or (c + dc) < 0):
                        temp[0] = 1
                        continue

                    if ((r + dr) == Rows or (c + dc) == Cols):
                        temp[1] = 1
                        continue

                    r_new = r + dr
                    c_new = c + dc

                    if ((r_new, c_new) not in visit and heights[r_new][c_new] <= heights[r][c]):
                        stack.append((r_new, c_new))
                        visit.add((r_new, c_new))

            return temp

        for i in range(Rows):
            for j in range(Cols):
                temp = dfs(i, j)
                if temp == [1, 1]:
                    # print("Hi ",i," ",j)
                    res.append([i, j])

        return res

