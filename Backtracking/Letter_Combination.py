class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        res = []
        temp_str = ""
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return res

        def dfs(dig_ind, temp_str):
            if len(temp_str) == len(digits):
                res.append(temp_str)
                return

            for ch in d[digits[dig_ind]]:
                dfs(dig_ind + 1, temp_str + ch)

            return

        dfs(0, "")
        return res


