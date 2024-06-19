class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while True:
            if n == 1:
                return res + 1

            else:
                if n % 2:
                    res += 1
                n = n // 2
