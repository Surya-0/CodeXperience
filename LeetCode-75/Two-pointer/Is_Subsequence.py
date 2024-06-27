class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        if not s:
            return True
        while r < len(t):
            if s[l] == t[r]:
                l += 1

            if l == len(s):
                return True

            r += 1

        return l == len(s)

