class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        new_range = n // 2
        res = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                res.append(i)

        res.append(n)
        if k > len(res):
            return -1
        else:
            return res[k - 1]