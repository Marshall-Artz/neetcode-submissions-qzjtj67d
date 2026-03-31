# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 1
        if root:
            return m + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
        