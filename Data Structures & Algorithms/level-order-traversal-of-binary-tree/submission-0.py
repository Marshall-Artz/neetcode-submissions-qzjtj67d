# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            res.append(node.val for node in stack)

            temp = []

            for i, node in enumerate(stack):
                if not node:
                    stack.pop(i)
                    continue
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            stack = temp
        
        return res