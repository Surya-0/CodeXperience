class Solution:
    def missingNumber(self, nums: 'List[int]') -> int:
        n = len(nums)
        res = 0
        for i in range(n + 1):
            res = res ^ i

        for i in nums:
            res = res ^ i

        return res


class Solution2:
    def missingNumber(self, nums: 'List[int]') -> int:
        n = len(nums)
        s = n * (n + 1) / 2

        arr_s = 0
        for i in nums:
            arr_s += i

        return int(s - arr_s)

