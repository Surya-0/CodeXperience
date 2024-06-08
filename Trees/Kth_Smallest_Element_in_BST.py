# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: 'Optional[TreeNode]', k: int) -> int:
        def inorder_traversal(root, val_arr):
            if root is None:
                return

            print("The value is : ", root.val)

            inorder_traversal(root.left, val_arr)
            val_arr.append(root.val)
            inorder_traversal(root.right, val_arr)

            return

        res = []
        inorder_traversal(root, res)

        return res[k - 1]