# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: bool) -> Optional[ListNode]:
        if not l1 and not l2:
            if carry:
                return ListNode(1)
            return None
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        c = 1 if carry else 0
        v = v1 + v2 + c

        node = ListNode(v % 10)
        node.next = self.solve(l1.next if l1 else None, l2.next if l2 else None, v >= 10)
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve(l1, l2, False)
        