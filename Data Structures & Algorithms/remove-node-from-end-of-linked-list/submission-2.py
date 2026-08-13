# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
 
        count = n

        lag, curr = None, prev
        for _ in range(n - 1):     # advance to the node you want to remove
            lag = curr
            curr = curr.next
        if lag is None:            # removing the head itself (n == 1)
            prev = curr.next   # new head of the reversed list
        else:
            lag.next = curr.next
            

        before, current = None, prev

        while current:
            nxt = current.next
            current.next = before
            before = current
            current = nxt

        return before