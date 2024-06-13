# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: 'Optional[ListNode]', left: int, right: int) -> 'Optional[ListNode]':
        dummy = ListNode(0, head)

        leftprev = dummy
        cur = head

        # First we reach the node at position left
        for i in range(left - 1):
            leftprev = cur
            cur = cur.next

        # Now cur = left, leftPrev = node before left
        # Reverse from left to right

        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next




