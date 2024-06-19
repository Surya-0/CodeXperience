class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        for i in range(x + 1):
            if i * i < x:
                res = i

            elif i * i == x:
                res = i
                return res

            else:
                return res

        return res