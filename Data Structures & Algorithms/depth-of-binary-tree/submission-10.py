# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        mx = 1

        while stack:
            cur = stack.pop()
            if cur[0].left:
                mx = max(mx, 1 + cur[1])
                stack.append((cur[0].left, 1 + cur[1]))
            if cur[0].right:
                mx = max(mx, 1 + cur[1])
                stack.append((cur[0].right, 1 + cur[1]))
        
        return mx
            