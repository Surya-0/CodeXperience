class Solution:
    def canPartition(self, nums: 'List[int]') -> bool:
        if len(nums) == 0:
            return True

        s = sum(nums)
        target = s // 2
        if (s % 2) or (len(nums) == 1):
            return False

        solverDP = set()
        solverDP.add(0)
        for i in range(len(nums)):
            tempDP = set()
            for ele in solverDP:
                tempDP.add(ele + nums[i])
                tempDP.add(ele)
            solverDP = tempDP

        return target in solverDP


