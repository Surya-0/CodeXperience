# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        mid = length // 2

        dummy = ListNode(val = 0,next = head)
        prev = dummy
        cur = head

        while cur and mid != 0:
            cur = cur.next
            prev = prev.next
            mid -= 1

        prev.next = cur.next
        cur.next = None

        return dummy.next

