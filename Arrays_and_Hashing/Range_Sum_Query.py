from typing import List


class NumArray:
    # [-2,-2,1,-4,-2,-3]
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.res = [0] * len(self.nums)
        self.res[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.res[i] = self.res[i - 1] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.res[right]

        else:
            return self.res[right] - self.res[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)