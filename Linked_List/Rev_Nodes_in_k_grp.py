# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rev_arr(self, arr, i, j):
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
        return

    def reverseKGroup(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]':
        stack = []
        cur = head

        if not head or k == 0:
            return head

        while cur:
            stack.append(cur.val)
            cur = cur.next

        for i in range(0, len(stack), k):
            if i + k <= len(stack):
                # print(i," ",i+k)
                self.rev_arr(stack, i, i + k - 1)
        res_arr = []
        for i in stack:
            res_arr.append(ListNode(i))

        for i in range(len(res_arr) - 1):
            res_arr[i].next = res_arr[i + 1]
        return res_arr[0]

