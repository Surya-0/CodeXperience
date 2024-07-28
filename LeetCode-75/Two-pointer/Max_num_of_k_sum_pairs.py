class Solution:
    def maxOperations(self, nums: 'List[int]', k: int) -> int:
        res = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            res_sum = nums[l] + nums[r]
            if res_sum > k:
                r = r - 1
            elif res_sum < k:
                l = l + 1

            else:
                res += 1
                l = l + 1
                r = r - 1

        return res

