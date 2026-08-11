# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        
        res = []

        while list1 and list2:
            if list1.val <= list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next
        if list1:
            while list1:
                res.append(list1.val)
                list1 = list1.next
        if list2:
            while list2:
                res.append(list2.val)
                list2 = list2.next
        
        result = ListNode()
        result.val = res[0]
        curr = result
        for i in range(1, len(res)):
            curr.next = ListNode(res[i])  # create new node, attach it
            curr = curr.next              # move the "current" hand forward
        return result


        