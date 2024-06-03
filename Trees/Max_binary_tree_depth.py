# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: 'Optional[TreeNode]') -> int:
        if root == None:
            return 0

        # print("Hi val : ",root.val)

        # print("Hi left : ",root.left)
        l_depth = 1 + self.maxDepth(root.left)
        # print("Left depth is : ",l_depth)

        # print("Hi right : ",root.right)
        r_depth = 1 + self.maxDepth(root.right)
        # print("Right depth is : " ,r_depth)

        # print("--------------------")
        return max(l_depth, r_depth)