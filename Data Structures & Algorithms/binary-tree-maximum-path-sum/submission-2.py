# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')

        def maxPathSumRec(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            # We only take the path from a child if it adds value (is > 0)
            leftMax = max(maxPathSumRec(root.left), 0)
            rightMax = max(maxPathSumRec(root.right), 0)
            
            # Potential path through this node acting as the highest peak (arc)
            current_path_sum = root.val + leftMax + rightMax
            
            # Update the global maximum
            self.max_val = max(self.max_val, current_path_sum)
            
            # Return the maximum single branch sum to the parent
            return root.val + max(leftMax, rightMax)

        maxPathSumRec(root)
        return self.max_val