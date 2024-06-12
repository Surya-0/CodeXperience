class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        Rows = len(board)
        Cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if ((r < 0 or c < 0) or (r == Rows or c == Cols) or (word[i] != board[r][c]) or (r, c) in path):
                return False

            path.add((r, c))

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            path.remove((r, c))

            return res

        for i in range(Rows):
            for j in range(Cols):
                if dfs(i, j, 0):
                    return True

        return False

