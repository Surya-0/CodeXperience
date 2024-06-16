class Solution:
    def solve(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        Rows = len(board)
        Cols = len(board[0])
        visit = set()
        queue = []

        def bfs(r, c):
            queue.append((r, c))
            visit.add((r, c))
            store = [(r, c)]
            t = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                r, c = queue.pop(0)
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if (((r_new, c_new) not in visit) and (r_new in range(Rows)) and (c_new in range(Cols)) and
                            board[r_new][c_new] == "O"):
                        store.append((r_new, c_new))
                        if ((r_new == 0 or r_new == Rows - 1) or (c_new == 0 or c_new == Cols - 1)):
                            t = 1
                        visit.add((r_new, c_new))
                        queue.append((r_new, c_new))

            if t == 0:
                return store
            else:
                return []

        def change_grid(mat):
            if mat == []:
                return

            for i, j in mat:
                board[i][j] = "X"
            return

        for r in range(1, Rows - 1):
            for c in range(1, Cols - 1):
                if ((r, c) not in visit and board[r][c] == "O"):
                    temp = bfs(r, c)
                    change_grid(temp)
