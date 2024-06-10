class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = set()
        col_num = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_num.add(i)
                    col_num.add(j)

        for i in range(n):
            for j in range(m):
                if i in row_num or j in col_num:
                    matrix[i][j] = 0


