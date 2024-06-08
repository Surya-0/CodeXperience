# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: 'TreeNode') -> int:
        max_val = -100000
        count_arr = [0]

        def dfs(root, max_val):
            if root is None:
                return

            if root.val >= max_val:
                count_arr[0] += 1
                max_val = max(root.val, max_val)

            dfs(root.left, max_val)
            dfs(root.right, max_val)

            return

        dfs(root, max_val)

        return count_arr[0]
