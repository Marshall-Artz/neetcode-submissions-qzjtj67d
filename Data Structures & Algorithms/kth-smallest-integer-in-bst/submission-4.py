# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k

        def kthSmallestRec(node: Optional[TreeNode]) -> list:
            if not node:
                return []
            
            left = kthSmallestRec(node.left)
            if type(left) == int:
                return left

            self.count -= 1
            if self.count == 0:
                return node.val

            right = kthSmallestRec(node.right)
            if type(right) == int:
                return right
            
            return  left + [node.val] + right
        return kthSmallestRec(root)