class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # left sorted position
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1

                else:
                    high = mid - 1

            # right sorted position
            else:
                if target > nums[mid] and target > nums[high]:
                    high = mid - 1

                elif target < nums[mid]:
                    high = mid - 1

                else:
                    low = mid + 1

        return -1