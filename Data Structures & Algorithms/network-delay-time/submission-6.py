class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's!

        adj = defaultdict(list)

        for ui, vi, ti in times:
            adj[ui].append((ti, vi))
        
        heap = []

        for edge, nextNode in adj[k]:
            heapq.heappush(heap, (edge, nextNode))

        vis = set()
        val = 0

        vis.add(k)

        while heap:
            edge, nextNode = heapq.heappop(heap)

            if nextNode in vis:
                continue
            
            vis.add(nextNode)
            val = max(val, edge)

            for nextEdge, nextNextNode in adj[nextNode]:
                heapq.heappush(heap, (edge + nextEdge, nextNextNode))
        
        return val if len(vis) == n else -1

        # times = [
        #     [1,2,1],
        #     [2,3,1],
        #     [1,4,4],
        #     [3,4,1]
        # ]
        # n = 4
        # k = 1
        # adj   = {
        #     1: [(1,2),(4,4)]
        #     2: [(1,3)]
        #     3: [(1,4)]
        # }

        # vis  = {
        #     1,
        #     2,
        #     3,
        #     4
        # }
        # heap = [
        #     /(4,4)
        # ]
        
        # val  = 3