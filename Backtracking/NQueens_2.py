class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        arr = [['.' for i in range(n)] for j in range(n)]

        col_set = set()  # The column set
        pos_diag_set = set()  # The right to left diagonal set storing (r+c)
        neg_diag_set = set()  # The left to right diagonal set storing (r-c)

        def nqueens(r):
            if r == n:
                res.append(arr)
                return

            for c in range(n):
                if ((c in col_set) or ((r - c) in neg_diag_set) or ((r + c) in pos_diag_set)):
                    continue

                arr[r][c] = 'Q'
                col_set.add(c)
                pos_diag_set.add(r + c)
                neg_diag_set.add(r - c)

                nqueens(r + 1)

                arr[r][c] = '.'
                col_set.remove(c)
                pos_diag_set.remove(r + c)
                neg_diag_set.remove(r - c)

            return

        nqueens(0)
        return len(res)

