# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root Left Right
        res = []

        def dfs(root):
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)
        return res