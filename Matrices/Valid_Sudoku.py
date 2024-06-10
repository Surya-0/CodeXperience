from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        rows = defaultdict(set)  # the key is the row no and the value is a set
        cols = defaultdict(set)  # the key is the col no and the value is a set
        mat = defaultdict(set)  # the key -> (row/3,col/3) and value -> set

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in mat[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                mat[(r // 3, c // 3)].add(board[r][c])

        return True