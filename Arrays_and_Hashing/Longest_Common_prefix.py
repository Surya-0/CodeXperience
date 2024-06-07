class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if len(strs) == 1:
            return strs[0]

        for i in range(0, len(strs) - 1):
            l = 0
            r = 0
            res = ""
            length = min(len(strs[i]), len(strs[i + 1]))
            while l < length and r < length:
                if strs[i][l] == strs[i + 1][r]:
                    res += strs[i][l]
                    l += 1
                    r += 1
                else:
                    break
            if res == "":
                return res
            strs[i + 1] = res

        return res