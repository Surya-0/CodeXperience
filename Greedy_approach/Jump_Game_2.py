from collections import deque
class Solution:
    def jump(self, nums: 'List[int]') -> int:
        res = 0
        # the left and right pointers represent the window
        l = 0
        r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(nums[i]+i,farthest)
            l = r+1
            r = farthest
            res +=1
        return res