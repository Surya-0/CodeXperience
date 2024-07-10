# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        dummy2 = ListNode(val=0)
        first = dummy2
        cur = head
        l = 0
        while cur:
            first.next = ListNode(val=cur.val)
            first = first.next
            cur = cur.next
            l += 1
        ptr1 = dummy2.next

        # print(ptr1)
        # print(head)

        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        ptr2 = prev
        n = l // 2

        # print(ptr1)
        # print(ptr2)
        # print(n)
        res = 0
        while n:
            res = max(ptr1.val + ptr2.val, res)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            n -= 1

        return res