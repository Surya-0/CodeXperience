# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [0]

        def lca(root, p, q):
            if not root:
                return 0

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            check_root = 0
            if root == p or root == q:
                check_root = 1

            total = check_root + left + right
            if total == 2:
                res.append(root)

            return total

        lca(root, p, q)
        return res[1]

