class Solution:
    def combine(self, n: int, k: int) -> 'List[List[int]]':
        res = []
        numbers = [i for i in range(1, n + 1)]
        subset = []

        def dfs(ind):
            if len(subset) == k:
                res.append(subset.copy())
                return

            if ind >= n:
                return

            subset.append(numbers[ind])
            dfs(ind + 1)

            subset.pop()
            dfs(ind + 1)

            return

        dfs(0)
        return res