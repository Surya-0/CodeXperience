# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: 'Optional[TreeNode]') -> bool:

        def dfs(root, left_val, right_val):
            if root is None:
                return True

            if not (root.val > left_val and root.val < right_val):
                return False

            # print("The value of the root is : ",root.val)
            left = dfs(root.left, left_val, root.val)
            right = dfs(root.right, root.val, right_val)

            # print("From the left for ",root.val," we have ",left)
            # print("From the right for ",root.val," we have ",right)

            return left and right

        return dfs(root, float('-inf'), float('inf'))


