# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        maxDepth = 1
        res      = [(root, maxDepth)]
        stack    = [(root, maxDepth)]

        while stack:
            cur = stack.pop()
            if cur[1] > maxDepth:
                maxDepth = cur[1]
                res.append(cur)
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                stack.append((cur[0].right, cur[1] + 1))
        
        for i, val in enumerate(res):
            print("node:", val[0].val, " depth:", val[1])
            res[i] = val[0].val

        
        return res