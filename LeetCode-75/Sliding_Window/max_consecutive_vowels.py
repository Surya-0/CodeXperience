class Solution:
    def longestOnes(self, nums: 'List[int]', k: int) -> int:
        l = 0
        r = 0
        c = 0
        max_res = 0
        while r < len(nums):
            if nums[r] == 0:
                # print("Right pointer : ",r)
                if c == k:
                    while c == k:
                        if nums[l] == 0:
                            c -= 1
                        l += 1

                    c += 1

                else:
                    c += 1

            # print(l," ",r," ",r - l + 1," ",c)
            max_res = max(max_res, r - l + 1)
            r += 1

        return max_res





