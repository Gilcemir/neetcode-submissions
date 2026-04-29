# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        head_r = head
        h = l // 2 if l % 2 == 0 else l // 2 + 1

        for i in range(h - 1):
            head_r = head_r.next
        
        # Unlink both lists
        temp = head_r.next
        head_r.next = None
        head_r = temp


        # reverse half of the linked list
        prev, curr = None, head_r
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head_r = prev

        p1, p2 = head, head_r

        
        while p1 and p2:
            print("p1:", p1.val, "p2:", p2.val)
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        """  
        
        while p1:
            print(p1.val)
            p1 = p1.next
        
        print("---")
        
        while p2:
            print(p2.val)
            p2 = p2.next
        """
        