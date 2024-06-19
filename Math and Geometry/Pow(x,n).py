class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            temp = power(x, n // 2)
            temp = temp * temp

            # for odd nos
            if n % 2:
                return temp * x

            # for even nos
            else:
                return temp

        res = power(x, abs(n))
        if n >= 0:
            return res

        else:
            return 1 / res
