from typing import List


class Solution:

    def isPali(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l = l + 1
                r = r - 1

            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):

            # print("This is dfs of : ",i)
            if i >= len(s):
                res.append(part.copy())
                # print("Res is : ",res)
                return

            for j in range(i, len(s)):

                if self.isPali(s, i, j):
                    # print("i : ",i," j : ",j)
                    part.append(s[i:j + 1])
                    # print("part is : ",part)
                    dfs(j + 1)
                    # print("We have returned from dfs of",j+1)
                    part.pop()

                # else:
                # print(s[i:j+1])
            # print("Returning part : ",part)
            return

        dfs(0)
        return res