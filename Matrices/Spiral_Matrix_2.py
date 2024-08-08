from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n
        top = 0
        bottom = n
        val = 1
        res = [[0 for i in range(n)] for j in range(n)]
        while top < bottom and left < right:
            # Move from left to right and record values from the top row
            for i in range(left, right):
                res[top][i] = val
                val += 1
            # shift the top row by 1 place to the bottom
            top += 1

            # Move from right top to the right bottom
            for i in range(top, bottom):
                res[i][right - 1] = val
                val += 1

            right -= 1

            if not (left < right and top < bottom):
                break

            # Move from right bottom to left bottom
            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = val
                val += 1

            bottom -= 1

            # Move from left bottom to left top as much as possible
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = val
                val += 1

            left += 1

        return res


