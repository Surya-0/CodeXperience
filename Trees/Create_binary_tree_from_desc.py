# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        childSet = set()
        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in node_map:
                node_map[parentVal] = TreeNode(parentVal)

            parent = node_map[parentVal]

            if childVal not in node_map:
                node_map[childVal] = TreeNode(childVal)
            child = node_map[childVal]

            if isLeft:
                parent.left = child

            else:
                parent.right = child

            childSet.add(childVal)

        rootVal = (set(node_map.keys()) - childSet).pop()
        return node_map[rootVal]
