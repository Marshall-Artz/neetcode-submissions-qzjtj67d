class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)

        for src, dst in tickets:
            edges[src].append(dst)
        
        for src in edges:
            edges[src].sort()
        
        res = ["JFK"]
        def dfs(source: str) -> bool:
            if len(tickets) + 1 == len(res):
                return True

            for i, dest in enumerate(edges[source]):
                edges[source].pop(i)
                res.append(dest)

                if dfs(dest): return True
                
                edges[source].insert(i, dest)
                res.pop()
            
            return False

        dfs("JFK")
        return res