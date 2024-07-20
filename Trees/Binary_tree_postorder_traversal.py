# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Postorder -> Left Right Root
        res = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

            return

        dfs(root)
        return res