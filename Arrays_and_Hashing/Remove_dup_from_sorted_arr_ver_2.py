class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        c = 1
        for i in range(1, len(nums)):
            if nums[k] == nums[i] and c < 2:
                c += 1
                k += 1
                nums[k] = nums[i]

            elif nums[k] == nums[i] and c >= 2:
                pass

            else:
                k += 1
                nums[k] = nums[i]
                c = 1
        nums = nums[:k + 1]
        print(nums)

        return len(nums)