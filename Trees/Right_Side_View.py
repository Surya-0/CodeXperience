# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: 'Optional[TreeNode]') -> 'List[int]':

        if root is None:
            return []

        def level_order_traversal(root):
            queue = [root]
            res = []

            while queue:
                q_len = len(queue)
                level = []
                for i in range(q_len):
                    node = queue.pop(0)
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)

                    if node.right is not None:
                        queue.append(node.right)

                res.append(level)

            return res

        rhs_view = level_order_traversal(root)
        result = []
        if rhs_view == [[]]:
            return result
        else:
            for i in range(len(rhs_view)):
                result.append(rhs_view[i].pop(-1))
            return result

