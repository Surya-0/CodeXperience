from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        def bfs(root):
            queue.append(root)
            res_sum = float('-inf')
            max_lvl = 0
            lvl = 0
            while queue:
                temp_sum = 0
                len_q = len(queue)
                # runs for an entire level
                for i in range(len_q):
                    node = queue.popleft()
                    temp_sum += node.val
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                lvl += 1
                if temp_sum > res_sum:
                    res_sum = temp_sum
                    max_lvl = lvl

            return max_lvl

        return bfs(root)

