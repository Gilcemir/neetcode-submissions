# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, m: int) -> int:
            if not root:
                return 0
            
            v = 1 if root.val >= m else 0
            # print("root: ", root.val, "v: ", v)
            current_m = max(root.val, m)
            return v + dfs(root.left, current_m) + dfs(root.right, current_m)
        
        return dfs(root, -101)

