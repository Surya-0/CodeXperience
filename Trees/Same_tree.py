# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: 'Optional[TreeNode]', q: 'Optional[TreeNode]') -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

        # def in_order(root):

        #     if root:
        #         arr = []
        #         left = post_order(root.left)
        #         right = post_order(root.right)
        #         arr.extend(left)
        #         arr.append(root.val)
        #         arr.extend(right)
        #         return arr
        #     else:
        #         return []
        # p_arr = post_order(p)
        # q_arr = post_order(q)
        # if p_arr == q_arr :
        #     return True
        # else:
        #     return False