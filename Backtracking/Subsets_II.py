class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        subset = []
        nums.sort()

        def dfs(ind):
            if ind >= len(nums):
                res.append(subset[::])
                return

            subset.append(nums[ind])
            dfs(ind + 1)

            # Not including nums[i]
            subset.pop()
            # This is the main part
            while (ind + 1) < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1
            dfs(ind + 1)
            return

        dfs(0)
        return res