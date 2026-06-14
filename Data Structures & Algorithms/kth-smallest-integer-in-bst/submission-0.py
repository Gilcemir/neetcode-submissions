# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s, res, curr = [], [], root

        while curr or len(s) > 0:

            while curr:
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            res.append(curr.val)

            curr = curr.right # if curr == None, stack will be pop'ed for the next iteration
            if len(res) == k:
                break

        return res[k - 1]
        