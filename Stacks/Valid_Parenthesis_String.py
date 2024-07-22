class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack1.append(i)

            elif ch == ")":
                if stack1:
                    stack1.pop()
                else:
                    if not stack2:
                        return False
                    stack2.pop()
            else:
                stack2.append(i)

        while stack1:
            if not stack2:
                return False
            elif stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()

            else:
                return False

        return True