# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRec(self, root: Optional[TreeNode], mn: Optional[TreeNode], mx: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if mx:
            if root.val >= mx.val:
                return False
            if root.right and root.right.val >= mx.val:
                return False
        
        if mn:
            if root.val <= mn.val:
                return False
            if root.left and root.left.val <= mn.val:
                return False

        
        return self.isValidBSTRec(root.left, mn, root) and self.isValidBSTRec(root.right, root, mx)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isValidBSTRec(root.left, None, root) and self.isValidBSTRec(root.right, root, None)
