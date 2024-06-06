class Solution:
    def romanToInt(self, s: str) -> int:
        m = ""
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ser = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] in ser:
                if m in ser[s[i]]:
                    res = res - d[s[i]]
                    m = s[i]

                else:
                    res = res + d[s[i]]
                    m = s[i]
            else:
                res = res + d[s[i]]
                m = s[i]

        return res
