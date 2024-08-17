from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        temp_row = points[0]

        for r in range(1, rows):
            next_row = points[r].copy()
            left, right = [0] * cols, [0] * cols
            left[0] = temp_row[0]

            # First populate from left to right based on the max values
            for c in range(1, cols):
                left[c] = max(temp_row[c], left[c - 1] - 1)

            right[cols - 1] = temp_row[cols - 1]

            # Next populate from right to left based on the max values
            for c in range(cols - 2, -1, -1):
                right[c] = max(temp_row[c], right[c + 1] - 1)

            for c in range(cols):
                next_row[c] += max(left[c], right[c])

            temp_row = next_row

        return max(temp_row)