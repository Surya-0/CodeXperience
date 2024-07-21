from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        ptr1 = 0
        ptr2 = 0
        while ptr1 < n and ptr2 < n:
            while stack and stack[-1] == popped[ptr2]:
                stack.pop()
                ptr2 += 1

            stack.append(pushed[ptr1])
            ptr1 += 1

        while ptr2 < n:
            if stack[-1] != popped[ptr2]:
                return False

            stack.pop()
            ptr2 += 1

        return True