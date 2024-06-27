class Solution:
    def longestSubarray(self, nums: 'List[int]') -> int:
        max_res = 0

        if not nums:
            return max_res

        temp = 0
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] == 0:
                if temp == 1:
                    while temp == 1:
                        if nums[l] == 0:
                            temp -= 1
                        l += 1

                temp += 1

                # else:
                # temp += 1

            max_res = max(max_res, r - l - temp + 1)
            r = r + 1

        if temp == 0:
            return max_res - 1

        else:
            return max_res









