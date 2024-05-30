class Solution:
    def compare_dicts(self, d1, d2):
        for key in d1:
            if key not in d2 or d1[key] > d2[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        d1 = {}
        d2 = {}
        for i in t:
            d1[i] = t.count(i)
        res = {}
        minlen = float('inf')
        minstr = ""
        l = 0
        r = 0
        if len(s) < len(t):
            return ""

        while r < m:
            if self.compare_dicts(d1, d2) == True:

                while self.compare_dicts(d1, d2):
                    if minlen > r - l:
                        minstr = s[l:r]
                        minlen = r - l
                    if s[l] in d2:
                        d2[s[l]] -= 1
                    l = l + 1
            if s[r] in d1:
                d2[s[r]] = 1 + d2.get(s[r], 0)
            r = r + 1

        while self.compare_dicts(d1, d2):
            if minlen > r - l:
                minstr = s[l:r]
                minlen = r - l

            if s[l] in d2:
                d2[s[l]] -= 1
            l = l + 1

        return minstr

