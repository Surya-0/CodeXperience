from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # res = []
        # temp_str = ""
        # d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        # if len(digits) == 0:
        #     return res

        # def dfs(ind,temp_str):
        #     if len(temp_str) == len(digits):
        #         res.append(temp_str)
        #         return

        #     n = d[digits[ind]]
        #     for i in n:
        #         print(ind+1," ",temp_str+i)
        #         dfs(ind+1,temp_str+i)
        #         print("The index is : ",ind)

        #     return

        # dfs(0,temp_str)

        # return res

        res = []
        temp_str = ""
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(digits) == 0:
            return res

        def dfs(ind, temp_str):
            if len(temp_str) == len(digits):
                res.append(temp_str)
                return

            s = d[digits[ind]]
            for i in s:
                dfs(ind + 1, temp_str + i)

            return

        dfs(0, "")
        return res


