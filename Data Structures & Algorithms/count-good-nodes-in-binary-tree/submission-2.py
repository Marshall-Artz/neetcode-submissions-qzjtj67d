# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesRecursive(self, root: TreeNode, maxSeen: int) -> int:
        if not root:
            return 0

        count = 1 if root.val >= maxSeen else 0
        newMaxSeen = max(maxSeen, root.val)
        
        return count + self.goodNodesRecursive(root.left, newMaxSeen) + self.goodNodesRecursive(root.right, newMaxSeen)

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRecursive(root, root.val)