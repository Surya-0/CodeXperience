# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy1 = ListNode(val=0)
        # dummy2 = ListNode(val=0)
        # oddptr = dummy1
        # evenptr = dummy2
        # checker = 1
        # cur = head
        # while cur:
        #     # print(cur)
        #     if checker % 2 != 0:
        #         oddptr.next = ListNode(val=cur.val)
        #         oddptr = oddptr.next
        #     else:
        #         evenptr.next = ListNode(val=cur.val)
        #         evenptr = evenptr.next
        #
        #     checker += 1
        #     cur = cur.next
        #
        # oddptr.next = dummy2.next
        # # print(dummy1)
        # # print(dummy2)
        # return dummy1.next

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head



