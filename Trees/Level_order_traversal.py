# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: 'Optional[TreeNode]') -> 'List[List[int]]':
        if root is None:
            return []

        res = []
        queue = [root]
        while queue:
            level = []
            len_q = len(queue)
            for i in range(len_q):
                node = queue.pop(0)
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            res.append(level)

        return res