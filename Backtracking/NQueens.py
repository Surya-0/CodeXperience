class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        res = []
        temp_arr = [['.' for i in range(n)] for j in range(n)]

        col_set = set()  # stores the columns seen
        neg_diag_set = set()  # stores the diagonals from left to right (r-c)
        pos_diag_set = set()  # stores the diagonals from right to left(r+c)

        def nqueens(r):
            if r == n:
                store = []
                for row in temp_arr:
                    store.append(''.join(row))
                res.append(store)
                return

            # iterate through the columns
            for c in range(n):
                if ((c in col_set) or ((r - c) in neg_diag_set) or ((r + c) in pos_diag_set)):
                    continue

                temp_arr[r][c] = 'Q'
                col_set.add(c)
                neg_diag_set.add(r - c)
                pos_diag_set.add(r + c)

                nqueens(r + 1)

                temp_arr[r][c] = '.'
                col_set.remove(c)
                neg_diag_set.remove(r - c)
                pos_diag_set.remove(r + c)

            return

        nqueens(0)
        return res





