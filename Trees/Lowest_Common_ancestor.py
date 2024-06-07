# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [root]

        # counter = [0]

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            root_check = 0
            final_res = 0

            if root == p or root == q:
                root_check = 1

            final_res = left + right + root_check

            if final_res == 2:
                res.append(root)

            return final_res

        dfs(root)
        # print(res[1])
        return res[1]
