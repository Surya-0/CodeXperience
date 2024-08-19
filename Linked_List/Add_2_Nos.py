# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res = []
        if len(stack2) > len(stack1):
            stack1, stack2 = stack2, stack1

        c = 0
        for i in range(len(stack2)):
            a = stack1[i]
            b = stack2[i]
            new_val = a + b + c
            if new_val >= 10:
                new_val = new_val - 10
                c = 1
            else:
                c = 0
            new_node = ListNode(new_val)
            res.append(new_node)

        for i in range(len(stack2), len(stack1)):
            a = stack1[i]
            new_val = a + c
            if new_val >= 10:
                new_val = new_val - 10
                c = 1
            else:
                c = 0
            new_node = ListNode(new_val)
            res.append(new_node)
        if c == 1:
            res.append(ListNode(1))

        for i in range(len(res) - 1):
            res[i].next = res[i + 1]

        return res[0]







