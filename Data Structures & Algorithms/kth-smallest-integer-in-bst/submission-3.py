# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def kthSmallestRec(root: Optional[TreeNode]) -> list:
            if not root:
                return []
            
            left = kthSmallestRec(root.left)
            if type(left) == int:
                return left
            
            self.count += 1
            if self.count == k:
                return root.val

            right = kthSmallestRec(root.right)
            if type(right) == int:
                return right
            
            return left + [root.val] + right

        return kthSmallestRec(root)