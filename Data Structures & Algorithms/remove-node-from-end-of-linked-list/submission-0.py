# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, length = None, 0

        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        prev_index = length - n
        #edge case: remover primeiro nó
        if prev_index == 0:
            return head.next
        
        curr = head
        for i in range(1, prev_index):
            curr = curr.next
        
        #print(curr.val)
        curr.next = curr.next.next

        return head