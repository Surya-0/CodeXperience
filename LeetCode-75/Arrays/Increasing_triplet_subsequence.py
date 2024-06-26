class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:
        var1 = max(nums)
        var2 = max(nums)
        for i in range(len(nums)):
            if nums[i] < var1:
                var1 = nums[i]

            elif var1 < nums[i] < var2:
                var2 = nums[i]

            elif nums[i] > var1 and nums[i] > var2:
                return True

        return False