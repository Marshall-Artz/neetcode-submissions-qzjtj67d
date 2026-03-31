class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(1, n + 1)]
        rank = [1] * n
        res = []

        def find(node):
            res = node

            while res != parent[res - 1]:
                res = parent[res - 1]
            
            return res
        
        def union(n1, n2):
            nonlocal res
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                res = [n1, n2]
                return True
            
            if rank[p1 - 1] >= rank[p2 - 1]:
                parent[p2 - 1] = p1
                rank[p1 - 1] += 1
            elif rank[p1 - 1] < rank[p2 - 1]:
                parent[p1 - 1] = p2
                rank[p2 - 1] += 1
            
            return False
            
        for n1, n2 in edges:
            union(n1, n2)
        return res