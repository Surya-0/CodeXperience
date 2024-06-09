# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: 'Optional[TreeNode]', targetSum: int) -> bool:
        cur = 0
        res = [False]

        def dfs(root, cur_sum):
            if root is None:
                return

            cur_sum += root.val

            if root.left is None and root.right is None:
                if cur_sum == targetSum:
                    res[0] = True

            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)

            return

        dfs(root, cur)
        return res[0]