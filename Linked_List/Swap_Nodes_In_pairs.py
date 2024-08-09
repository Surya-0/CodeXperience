# Definition for singly-linked list.
from  typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(val=0, next=head)
        prev = dummy
        cur = head
        while cur and cur.next:
            first_node = cur
            second_node = cur.next

            prev.next = second_node
            cur.next = second_node.next
            second_node.next = first_node

            prev = first_node
            cur = first_node.next

        return dummy.next
