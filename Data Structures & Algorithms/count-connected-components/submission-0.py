class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        def dfs(node, parent) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            for n in graph[node]:
                if n == parent:
                    continue
                dfs(n, node)
            return True
        
        # Load graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        numComponents = 0
        for node in range(n):
            if dfs(node, -1):
                numComponents += 1
        return numComponents