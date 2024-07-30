class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        closed_count = 0
        res = ""
        for i in range(len(s)):
            ch = s[i]
            if ch != "(" and ch != ")":
                res += ch

            elif ch == "(":
                open_count += 1
                res += ch

            elif open_count > 0:
                open_count -= 1
                res += ch

        if open_count > 0:
            s = res
            res = ""
            for i in range(len(s) - 1, -1, -1):
                ch = s[i]
                if ch != "(" and ch != ")":
                    res += ch

                elif ch == ")":
                    closed_count += 1
                    res += ch

                elif closed_count > 0:
                    closed_count -= 1
                    res += ch

            return res[::-1]
        return res
