from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        d = defaultdict(str)
        print(l)
        n = len(pattern)
        if n != len(l):
            return False

        for i in range(n):
            if d[pattern[i]]:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                d[pattern[i]] = l[i]
        print(d)
        return len(d.values()) == len(set(d.values()))