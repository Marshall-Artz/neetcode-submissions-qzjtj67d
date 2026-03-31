# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left and root.right:
                self.invertTree(root.left)
                self.invertTree(root.right)
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left and root.right == None:
                self.invertTree(root.left)
                root.right = root.left
                root.left = None
            elif root.left == None and root.right:
                self.invertTree(root.right)
                root.left = root.right
                root.right = None
        
        return root