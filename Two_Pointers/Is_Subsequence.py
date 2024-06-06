class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0  # for s
        p2 = 0  # for t
        length_t = len(t)
        length_s = len(s)

        print(length_s, " ", length_t)
        if length_s == 0:
            return True

        if length_t == 0:
            return False

        while p2 < len(t):
            if t[p2] == s[p1]:
                p1 = p1 + 1

            if p1 == length_s:
                return True
                break

            p2 = p2 + 1

        return False
