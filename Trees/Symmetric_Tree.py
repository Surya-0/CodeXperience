# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric_tree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        left = self.symmetric_tree(root1.left, root2.right)
        right = self.symmetric_tree(root1.right, root2.left)
        compare = left and right
        return (root1.val == root2.val) and compare

    def isSymmetric(self, root: 'Optional[TreeNode]') -> bool:

        res = self.symmetric_tree(root.left, root.right)
        return res