from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        n = len(s)
        d = defaultdict(str)
        for i in range(n):
            if d[s[i]]:
                if d[s[i]] != t[i]:
                    return False
            d[s[i]] = t[i]
        print(d.values())
        return len(d.values()) == len(set(d.values()))


