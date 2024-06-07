# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FoundSubtreeException(Exception):
    pass

class Solution:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool:
        def sameTree(root, subroot):
            if not root and not subroot:
                return True

            if not root or not subroot:
                return False

            left = sameTree(root.left, subroot.left)
            right = sameTree(root.right, subroot.right)
            compare = left and right

            return (root.val == subroot.val) and compare

        def dfs(root):
            if root is None:
                return

            if sameTree(root, subRoot):
                raise FoundSubtreeException()

            dfs(root.left)
            dfs(root.right)

        try:
            dfs(root)
            return False  # If we finished the DFS without finding the subtree, return False
        except FoundSubtreeException:
            return True  # If we caught the exception, it means we found the subtree, so return True