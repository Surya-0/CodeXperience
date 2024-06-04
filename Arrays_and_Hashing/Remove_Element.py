class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        k = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                k = k + 1
                nums[k] = nums[i]

        nums = nums[:k + 1]
        return len(nums)
