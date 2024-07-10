from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        l = [i for i in range(1, 10)]
        sub_arr = []

        def dfs(ind, sumer):
            if sumer == n and len(sub_arr) == k:
                res.append(sub_arr.copy())
                return

            if ind >= len(l) or sumer > n:
                return

            sub_arr.append(l[ind])
            dfs(ind + 1, sumer + l[ind])
            sub_arr.pop()
            dfs(ind + 1, sumer)

            return

        dfs(0, 0)
        return res


