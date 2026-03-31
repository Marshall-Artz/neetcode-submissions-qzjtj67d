# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> list:
            if not node:
                return []
            elif node and not node.left and not node.right:
                return [node.val]
            elif node.left and node and node.right:
                return dfs(node.left) + [node.val] + dfs(node.right)
            elif not node.left and node and node.right:
                return [node.val] + dfs(node.right)
            elif node.left and node and not node.right:
                return dfs(node.left) + [node.val]
        
        return dfs(root)