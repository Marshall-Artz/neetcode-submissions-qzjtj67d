# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        mem = {}
        def dfs(node: Optional[TreeNode], canRob: bool) -> int:
            if not node:
                return 0

            state = (node, canRob)
            res   = 0

            if state in mem:
                return mem[state]
            if canRob == False:
                res = dfs(node.left, True) + dfs(node.right, True)
            if canRob == True:
                res = max(
                    node.val + dfs(node.left, False) + dfs(node.right, False),
                    dfs(node.left, True) + dfs(node.right, True)
                )
            
            mem[state] = res

            return mem[state]
        
        return max(dfs(root, True), dfs(root, False))