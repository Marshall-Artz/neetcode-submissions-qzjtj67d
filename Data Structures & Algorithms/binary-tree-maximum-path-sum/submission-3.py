# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = float('-inf')

        def maxPathSumRec(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            # We only take the path from a child if it adds value (is > 0)
            leftVal = max(maxPathSumRec(root.left), 0)
            rightVal = max(maxPathSumRec(root.right), 0)
            print("for", root.val)
            print("leftVal:", leftVal)
            print("rightVal:", rightVal)

            # Potential path through this node acting as the highest peak (arc)
            completePath = leftVal + rightVal + root.val
            print("complete path:", completePath)

            # Update the global maximum
            self.maxVal = max(completePath, self.maxVal)
            print("maxVal?", self.maxVal)

            # Return the maximum single branch sum to the parent
            return max(leftVal + root.val, rightVal + root.val)
        
        maxPathSumRec(root)
        return self.maxVal
