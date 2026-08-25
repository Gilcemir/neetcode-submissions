"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new: dict[Optional['Node'], Optional['Node']] = {}

        def clone(nd: Optional['Node']) -> Optional['Node']:
            if nd is None:
                return None
            if nd in old_to_new:
                return old_to_new[nd]
            cp = Node(nd.val)
            old_to_new[nd] = cp
            for ngb in nd.neighbors:
                cp.neighbors.append(clone(ngb))
            
            return cp
        
        return clone(node)