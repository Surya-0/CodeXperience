# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: 'Optional[ListNode]', x: int) -> 'Optional[ListNode]':
        if head is None:
            return head

        left_dummy = ListNode()
        right_dummy = ListNode()

        left = left_dummy
        right = right_dummy

        cur = head
        while cur:
            # print("Current value : ",cur.val)
            # print(left)
            # print(right)
            if cur.val < x:
                left.next = cur
                left = left.next

            else:
                right.next = cur
                right = right.next

            cur = cur.next

        left.next = right_dummy.next
        right.next = None

        return left_dummy.next

