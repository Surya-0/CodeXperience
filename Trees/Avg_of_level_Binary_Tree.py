import statistics


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: 'Optional[TreeNode]') -> 'List[float]':
        def level_order(root):
            if root is None:
                return []

            queue = [root]
            res = []
            while queue:
                level = []
                num_len = len(queue)
                for i in range(num_len):
                    node = queue.pop(0)
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                res.append(statistics.mean(level))
            return res

        return level_order(root)
