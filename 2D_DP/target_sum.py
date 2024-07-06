from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index,total) -> # of ways

        def backtrack(ind, cur_tot):
            if ind == len(nums):
                return 1 if cur_tot == target else 0

            if (ind, cur_tot) in dp:
                return dp[(ind, cur_tot)]

            dp[(ind, cur_tot)] = (backtrack(ind + 1, cur_tot + nums[ind]) + backtrack(ind + 1, cur_tot - nums[ind]))

            return dp[(ind, cur_tot)]

        res = backtrack(0, 0)
        print(dp)
        return res
