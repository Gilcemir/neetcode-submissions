# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevTail = dummy

        while True:
            kth = self.getKth(prevTail, k)
            if not kth:
                break
            
            nextHead = kth.next

            prev, curr = nextHead, prevTail.next
            while curr != nextHead:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevTail.next
            prevTail.next = kth
            prevTail = tmp

        return dummy.next


        
        
        