"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copies = {}
        def dfs(originalNode: Optional['Node']) -> Optional['Node']:
            if not originalNode:
                return None
            if originalNode in copies:
                return copies[originalNode]
            
            copy = Node(originalNode.val, [])
            copies[originalNode] = copy

            for originalNeighbor in originalNode.neighbors:
                copy.neighbors.append(dfs(originalNeighbor))
            
            return copy

        return dfs(node)