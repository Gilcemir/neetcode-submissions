"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = dict()
        curr = head
        while curr:
            copy = Node(curr.val)
            m[curr] = copy
            curr = curr.next
        
        for orig, copy in m.items():
            copy.next = m[orig.next] if orig.next else None
            copy.random = m[orig.random] if orig.random else None
        
        return m[head] if head else None