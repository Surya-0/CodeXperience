class Solution:
    def rob(self, nums: 'List[int]') -> int:
        rob1 = 0
        rob2 = 0
        # Solving using bottom up approach
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2