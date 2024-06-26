class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        # print(n," ",m)

        # First take the transpose
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each of these rows
        for row in matrix:
            row.reverse()




