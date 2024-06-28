class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        if not s:
            return res
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)

            elif i == "*":
                stack.pop()

        res = ''.join(stack)
        return res