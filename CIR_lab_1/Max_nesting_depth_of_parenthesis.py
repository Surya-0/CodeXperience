class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
                res = max(res, len(stack))

            elif i == ")":
                stack.pop()

        return res