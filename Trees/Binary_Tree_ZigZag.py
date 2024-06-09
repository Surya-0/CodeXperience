# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: 'Optional[TreeNode]') -> 'List[List[int]]':

        def level_order(root):
            if root is None:
                return []

            queue = [root]
            res = []
            c = 0
            while queue:
                level = []
                num_len = len(queue)
                for i in range(num_len):
                    node = queue.pop(0)
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)

                    if node.right is not None:
                        queue.append(node.right)
                if c % 2 == 0:
                    res.append(level)
                else:
                    level.reverse()
                    res.append(level)
                c += 1

            return res

        return level_order(root)

