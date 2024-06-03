# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: 'Optional[TreeNode]') -> bool:

        flag = [True]

        def height_check(root):
            if root == None:
                return 0

            # print("Hi val : ",root.val)

            # print("Hi left : ",root.left)
            l_depth = 1 + height_check(root.left)
            # print("left depth : ",l_depth)

            # print("Hi right : ",root.right)
            r_depth = 1 + height_check(root.right)
            # print("right depth : ",r_depth)

            if abs(r_depth - l_depth) >= 2:
                flag[0] = False

            return max(l_depth, r_depth)

        height_check(root)
        return flag[0]


