class Solution:
    def isHappy(self, n: int) -> bool:
        def calcSquare(n):
            res = 0
            while n:
                a = n % 10
                n = n // 10
                res += a * a
            return res

        counter = n
        myset = set()
        while True:
            if n in myset:
                return False

            myset.add(n)
            n = calcSquare(n)
            if n == 1:
                return True
