from collections import deque

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        def bfs(root):
            temp = deque()
            temp.append(root)
            while temp:
                n = len(temp)
                level = []
                for i in range(n):
                    node = temp.popleft()
                    level.append(node.val)
                    if node.left:
                        temp.append(node.left)

                    if node.right:
                        temp.append(node.right)
                res.append(level)

        bfs(root)
        res.reverse()
        return res


