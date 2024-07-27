o# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool:
        res = [False]

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
            if root is None or res[0]:
                return

                # print(root.val)
            if sameTree(root, subRoot):
                res[0] = True
                return

            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        return res[0]