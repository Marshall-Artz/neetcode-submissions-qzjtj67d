"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(n: Optional['Node']) -> Optional['Node']:
            if not n:
                return None
            
            copy = Node(n.val)
            visited[n.val] = copy

            for i in range(len(n.neighbors)):
                if n.neighbors[i].val not in visited:
                    copy.neighbors.append(dfs(n.neighbors[i]))
                elif n.neighbors[i].val in visited:
                    copy.neighbors.append(visited[n.neighbors[i].val])
            
            return copy

        return dfs(node)
