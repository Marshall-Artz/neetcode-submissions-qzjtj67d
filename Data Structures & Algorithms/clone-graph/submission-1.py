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
        
        def dfs(n: Optional['Node']):
            if not n or n in copies:
                return
            
            copies[n] = Node(n.val, [])

            for neighbor in n.neighbors:
                dfs(neighbor)
        
        dfs(node)

        for n, copy in copies.items():
            copyNeighbors = []
            for neighbor in n.neighbors:
                copyNeighbors.append(copies[neighbor])
            copy.neighbors = copyNeighbors

        return copies[node]