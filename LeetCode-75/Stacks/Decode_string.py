class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)

            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                fact = ""
                while stack and stack[-1].isdigit():
                    fact = stack.pop() + fact

                # print(fact)
                fact = int(fact)
                stack.append(substr * fact)

        # print(stack)
        return ''.join(stack)




