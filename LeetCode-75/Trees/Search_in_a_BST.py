# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = [None]

        def dfs(root):
            if not root:
                return

            if val < root.val:
                dfs(root.left)

            elif val > root.val:
                dfs(root.right)

            else:
                res[0] = root

            return

        dfs(root)
        return res[0]

