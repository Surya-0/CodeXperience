from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)

        res = 0
        rem = 0
        for k, v in d.items():
            if v % 2 == 0:
                res += v

            else:
                res += v - 1
                rem = 1

        return res + rem