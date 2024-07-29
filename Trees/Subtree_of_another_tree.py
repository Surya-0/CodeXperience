# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isSameTree(self, root, subroot):
        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        left = self.isSameTree(root.left, subroot.left)
        right = self.isSameTree(root.right, subroot.right)

        return root.val == subroot.val and left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]

        def dfs(root):
            if root is None:
                return False

            if root.val == subRoot.val:
                if self.isSameTree(root, subRoot):
                    res[0] = True

            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)
        return res[0]


