class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        res = []
        cur = []

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or cur_sum > target:
                return

            cur.append(candidates[i])
            print("The cur is : ", cur)
            dfs(i, cur_sum + candidates[i])

            cur.pop()
            print("The cur is : ", cur)
            dfs(i + 1, cur_sum)

            return

        dfs(0, 0)
        return res


