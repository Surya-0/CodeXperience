class Solution:
    def findDuplicate(self, nums: 'List[int]') -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, "\t", fast)
            if slow == fast:
                break
        print(slow, " ", fast)

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        print(slow, " ", slow2)
        return slow
