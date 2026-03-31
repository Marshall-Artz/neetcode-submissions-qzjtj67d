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

        def buildTreeRec(preorder: List[int], inorder: List[int], in_start: int) -> Optional[TreeNode]:
            if not preorder:
                return None
            
            root = TreeNode(preorder[0], None, None)
            index = self.dic[root.val]

            # Number of elements in the left subtree
            left_size = index - in_start
            
            inOrderLeft  = inorder[:left_size]
            inOrderRight = inorder[left_size+1:]
            
            preOrderLeft  = preorder[1:left_size+1]
            preOrderRight = preorder[left_size+1:]

            root.left = buildTreeRec(preOrderLeft, inOrderLeft, in_start)
            root.right = buildTreeRec(preOrderRight, inOrderRight, index + 1)

            return root
        return buildTreeRec(preorder, inorder, 0)