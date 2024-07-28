from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            # If the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        # Close the last range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges