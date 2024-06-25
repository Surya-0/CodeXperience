class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for string in s:
            if stack and stack[-1] == string:
                stack.pop()
                string = ""

            if string:
                stack.append(string)

        return ''.join(stack)
