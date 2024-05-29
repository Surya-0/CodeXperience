class Solution:
    def compare_dicts(self, d1, d2):
        for key in d1:
            if key not in d2 or d1[key] != d2[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        d = {}
        for i in s1:
            d[i] = s1.count(i)

        l = 0
        r = 0
        res = {}
        while r < len(s2):

            if (r - l + 1) > k and self.compare_dicts(d, res):
                return True

            if (r - l + 1) > k and not (self.compare_dicts(d, res)):
                res[s2[l]] -= 1
                l += 1

            if (r - l + 1) <= k:
                res[s2[r]] = 1 + res.get(s2[r], 0)
                r += 1

            # print(l," ",r," ",res)

        return self.compare_dicts(d, res)


