from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = rStart, cStart
        res = []
        step = 1
        i = 0
        while len(res) < rows * cols:
            for _ in range(2):
                dr, dc = directions[i]
                for _ in range(step):
                    if r in range(rows) and c in range(cols):
                        res.append([r, c])
                    r = r + dr
                    c = c + dc

                i = (i + 1) % 4
            step += 1

        return res