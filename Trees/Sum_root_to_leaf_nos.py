# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr_sum = [0]

        def dfs(root, s):
            if root is None:
                return

            s += str(root.val)

            if root.left is None and root.right is None:
                arr_sum[0] += int(s)

            dfs(root.left, s)
            dfs(root.right, s)

            return

        s = ""
        dfs(root, s)
        return arr_sum[0]
