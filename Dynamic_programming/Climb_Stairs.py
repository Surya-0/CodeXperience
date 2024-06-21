class Solution:
    def climbStairs(self, n: int) -> int:

        # Bottom up approach as we are starting from the base case
        v_a = 1
        v_b = 1

        for i in range(n-1):
            temp = v_a
            v_a = v_a + v_b
            v_b = temp

        return v_a



class Solution2:
    def climbStairs(self, n: int) -> int:
        d = {}
        # lets try memoization where we have a top down approach coupled with recursion
        def climb_memo(n):
            if n in d:
                return d[n]

            if n <= 1:
                return 1

            d[n] = climb_memo(n - 1) + climb_memo(n - 2)
            return d[n]

        return climb_memo(n)