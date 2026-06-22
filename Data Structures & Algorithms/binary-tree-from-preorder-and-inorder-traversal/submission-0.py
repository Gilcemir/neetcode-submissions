# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self._map = {}
        for i, item in enumerate(inorder):
            self._map[item] = i

        self._idx = 0 # porque é uma "dfs, esse valor incrementa usando ordem in-order e "resolve"a arvore"
        def solve(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None

            value = preorder[self._idx]
            node = TreeNode(value)

            self._idx += 1
        
            node.left = solve(lo, self._map[value] - 1)
            node.right = solve(self._map[value] + 1, hi)

            return node

        return solve(0, len(inorder) - 1)

