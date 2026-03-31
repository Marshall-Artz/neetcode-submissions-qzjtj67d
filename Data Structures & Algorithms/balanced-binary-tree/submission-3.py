# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node) -> int:
            if not node:
                return 0
            
            l = self.maxDepth(node.left)
            r = self.maxDepth(node.right)

            if l == -1 or r == -1:
                return -1
            
            if abs(l - r) > 1:
                return -1
            
            return 1 + max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        if l == -1 or r == -1:
            return False
        
        if abs(l - r) > 1:
            return False
        
        return True