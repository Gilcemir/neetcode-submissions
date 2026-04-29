# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #neetcode solution:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        p1, p2 = head, prev
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1

            p1 = tmp1
            p2 = tmp2