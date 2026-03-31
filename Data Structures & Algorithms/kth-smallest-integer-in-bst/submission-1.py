# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallestRec(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        
        res = self.kthSmallestRec(root.left)
        res.append(root.val)
        res.extend(self.kthSmallestRec(root.right))
        
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kthSmallestRec(root)[k-1]