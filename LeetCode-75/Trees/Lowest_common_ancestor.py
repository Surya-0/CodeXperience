# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # res = []

        # def dfs(root):
        #     if root is None:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     root_check = 0
        #     if root == p or root == q:
        #         root_check += 1

        #     final_res = root_check + left + right

        #     if final_res == 2:
        #         res.append(root)

        #     return final_res

        # dfs(root)
        # return res[0]

        res = []

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            root_check = 0
            if root.val == p.val or root.val == q.val:
                root_check += 1

            final_res = root_check + left + right
            if final_res == 2:
                res.append(root)

            return final_res

        dfs(root)
        return res[0]


