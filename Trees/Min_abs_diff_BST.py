# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: 'Optional[TreeNode]') -> int:

        def inorder(root, val_arr):
            if root is None:
                return

            inorder(root.left, val_arr)
            val_arr.append(root.val)
            inorder(root.right, val_arr)

            return

        res = []
        inorder(root, res)
        min_val = 100000
        for i in range(len(res) - 1):
            min_val = min(min_val, abs(res[i + 1] - res[i]))
        return min_val
