class Solution:
    def maxProduct(self, nums: 'List[int]') -> int:
        cur_min = 1
        cur_max = 1
        res_max = max(nums)
        for n in nums:
            temp = cur_max
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(temp * n, cur_min * n, n)
            res_max = max(cur_max, res_max)

        return res_max