class Solution:
    def findPeakElement(self, nums: 'List[int]') -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # Check if mid is less than left neighbour,then shift the right pointer
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = r - 1

            # Check if mid is less than right neighbour,then shift the left pointer
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = l + 1

            else:
                return mid
