class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        # d = {}
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False


sol = Solution()
