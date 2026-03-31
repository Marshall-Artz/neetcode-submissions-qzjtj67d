class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()

        # Build graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, parent) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode == parent:
                    continue
                if not dfs(nextNode, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        if len(visited) != n:
            return False
        
        return True