from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        temp_q = deque([root])
        while temp_q:
            node = temp_q.popleft()
            if node:
                temp_q.append(node.left)
                temp_q.append(node.right)
            else:
                while temp_q:
                    if temp_q.popleft():
                        return False

        return True


