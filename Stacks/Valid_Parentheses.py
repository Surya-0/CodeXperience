class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            if i == ')':
                if stack != [] and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            if i == ']':
                if stack != [] and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            if i == '}':
                if stack != [] and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        else:
            return False