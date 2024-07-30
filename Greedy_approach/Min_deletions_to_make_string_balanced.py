class Solution:
    def minimumDeletions(self, s: str) -> int:
        # First let us create a suffix rep of a
        count_a = [0] * len(s)
        for i in range(len(s) - 2, -1, -1):
            count_a[i] = count_a[i + 1]
            count_a[i] += 1 if s[i + 1] == "a" else 0

        count_b = 0
        res = len(s)
        for i, val in enumerate(s):
            res = min(res, count_a[i] + count_b)
            if val == "b":
                count_b += 1

        return res


