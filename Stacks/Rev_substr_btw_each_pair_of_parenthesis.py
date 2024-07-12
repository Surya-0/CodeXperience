class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            temp = []
            # When we find a closing parenthesis
            if char == ")":

                # Pop till we get an opening bracket
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())

                # Pop the opening bracket
                stack.pop()

                stack.extend(temp)

            else:
                stack.append(char)

        return ''.join(stack)