from typing import List


class Solution:
    def luckyNumbers(self, matrix:
    List[List[int]]) -> List[int]:
        row_set = set()
        col_set = set()
        m = len(matrix)
        n = len(matrix[0])
        print(matrix, " ", len(matrix))
        for i in range(m):
            row_set.add(min(matrix[i]))

        for i in range(n):
            col_set.add(max([row[i] for row in matrix]))

        return list(row_set.intersection(col_set))