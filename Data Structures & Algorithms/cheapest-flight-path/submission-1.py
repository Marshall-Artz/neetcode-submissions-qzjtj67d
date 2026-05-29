class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build Graph:
        adj = defaultdict(list)

        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        
        visit   = set()
        minCost = float('inf')
        heap    = [(0, 0, src)]

        while heap:
            totalCost, stops, node = heapq.heappop(heap)
            visit.add(node)

            if node == dst:
                minCost = min(minCost, totalCost)
            
            if stops > k:
                continue

            for to_i, ticketPrice in adj[node]:
                # Check stops #
                if to_i not in visit:
                    heapq.heappush(heap, (totalCost + ticketPrice, stops + 1, to_i))
        
        return minCost if minCost != float('inf') else -1

        
        # flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
        # src, dst, k = 0, 3, 1
        # adj = {
        #     0: [(1,200)],
        #     1: [(2,100), (3,300)],
        #     2: [(3,100)]
        # }
        # visit   = {0, 1, 2, 3}
        # minCost = 500
        # heap    = []
        # totalCost, stops, node = 
