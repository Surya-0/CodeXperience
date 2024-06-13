# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rev_array(self, arr, i, j):

        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
        return arr

    def rotateRight(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]':
        cur = head
        stack = []
        if head is None or k == 0:
            return head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        k = k % len(stack)
        self.rev_array(stack, 0, len(stack) - 1)
        self.rev_array(stack, 0, k - 1)
        self.rev_array(stack, k, len(stack) - 1)
        # print(stack)
        stack2 = []
        for i in stack:
            stack2.append(ListNode(val=i))
        for i in range(len(stack2) - 1):
            stack2[i].next = stack2[i + 1]
        # print("Stack 2 : ",stack2)
        return stack2[0]