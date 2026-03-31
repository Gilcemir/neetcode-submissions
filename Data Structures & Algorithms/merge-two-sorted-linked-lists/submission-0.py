# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        p1, p2, head = list1, list2, None

        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next

        curr = head
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                curr = p1
                p1 = p1.next
            else:
                curr.next = p2
                curr = p2
                p2 = p2.next
        
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2

        return head

        