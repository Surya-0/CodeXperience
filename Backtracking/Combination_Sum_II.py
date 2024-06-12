class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        res = []
        subset = []
        candidates.sort()

        def dfs(ind, cur_sum):
            if cur_sum == target:
                res.append(subset.copy())
                return

            if ind >= len(candidates) or cur_sum > target:
                return

            subset.append(candidates[ind])
            dfs(ind + 1, cur_sum + candidates[ind])

            subset.pop()
            while (ind + 1) < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind = ind + 1
            dfs(ind + 1, cur_sum)

            return

        dfs(0, 0)
        return res

