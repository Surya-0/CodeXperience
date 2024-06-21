from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: 'Optional[TreeNode]') -> int:
        # For this problem we need to perform a BFS and we can
        # probably assign numbers to each of the node left -> 2*n right -> 2*n + 1

        res = 0  # Contains the max width
        temp_q = deque()
        temp_q.append((root, 1, 0))  # (node,number assigned,level)
        prev_num = 1  # contains the number of the first node in a level
        cur_lvl = 0  # Contains the current level which we are at
        while temp_q:
            node, num, lvl = temp_q.popleft()

            if lvl > cur_lvl:
                cur_lvl = lvl
                prev_num = num

            res = max(res, num - prev_num + 1)
            if node.left:
                temp_q.append((node.left, 2 * num, lvl + 1))

            if node.right:
                temp_q.append((node.right, 2 * num + 1, lvl + 1))

        return res
