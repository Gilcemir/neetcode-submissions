# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = [(root, -1001, 1001)]

        while q:
            node, minV, maxV = q.pop()
            if node.val >= maxV or node.val <= minV:
                return False
            
            if node.left:
                q.append((node.left, minV, min(maxV, node.val)))
            if node.right:
                q.append((node.right, max(minV, node.val), maxV))
        
        return True

        