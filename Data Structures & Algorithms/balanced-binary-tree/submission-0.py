# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(r: Optional[TreeNode]) -> int:
            if not r:
                return 0

            left = dfs(r.left)
            right = dfs(r.right)

            if abs(left - right) > 1:
                self.isBalanced = False

            return max(left, right) + 1
        
        dfs(root)
        return self.isBalanced

        