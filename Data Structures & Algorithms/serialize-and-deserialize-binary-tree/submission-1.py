# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        self.vals = data.split(',')
        self.i = 0
        print("vals:", self.vals)

        def dfs() -> Optional[TreeNode]:
            if self.vals[self.i] == "null":
                self.i += 1
                return None
            node = TreeNode(int(self.vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
