# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._map = {}
        def solve(root: Optional[TreeNode]) -> int:
            if not root:
                return -math.inf
            
            left = solve(root.left)
            right = solve(root.right)

            max_val_1 = max(
                root.val, 
                root.val + left, 
                root.val + right,
                )
            max_val_2 = max(max_val_1, root.val + left + right)
            self._map[root.val] = max_val_2, max_val_1
            return max_val_1
        
        solve(root)
        highests, _ = zip(*self._map.values())
        print(highests)
        return max(highests)
            
