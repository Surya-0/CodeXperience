# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         while part in s:
#             s = s.replace(part, '', 1)
#         return s

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            # If the end of the stack matches the part, remove it
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                for _ in range(part_len):
                    stack.pop()

        return ''.join(stack)