# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        cur = head
        res = {None:None}

        while cur:
            copy_node = Node(cur.val)
            res[cur] = copy_node
            cur = cur.next
        cur = head
        while cur:
            copy = res[cur]
            copy.next = res[cur.next]
            copy.random = res[cur.random]
            cur = cur.next

        return res[head]