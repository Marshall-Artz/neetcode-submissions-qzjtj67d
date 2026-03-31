# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.dic = {}
        for i, val in enumerate(inorder):
            self.dic[val] = i

        def buildTreeRec(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder:
                return None
            
            root = TreeNode(preorder[0], None, None)
            index = self.dic[root.val]
            
            inOrderLeft  = inorder[:index]
            inOrderRight = inorder[index+1:]
            
            preOrderLeft  = preorder[1:len(inOrderLeft)+1]
            preOrderRight = preorder[len(inOrderLeft)+1:]

            root.left = self.buildTree(preOrderLeft, inOrderLeft)
            root.right = self.buildTree(preOrderRight, inOrderRight)

            return root
        return buildTreeRec(preorder, inorder)