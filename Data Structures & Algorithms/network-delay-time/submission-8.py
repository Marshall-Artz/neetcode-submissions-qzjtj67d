class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        heap = [(0, k)]
        vis  = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in vis:
                continue

            vis.add(node)

            if len(vis) == n:
                return time

            for nextEdge, nextNode in adj[node]:
                heapq.heappush(heap, (time + nextEdge, nextNode))
        
        return -1

        # times = [[1,2,1],[2,3,1]], n = 3, k = 2
        # adj = {
        #     1: [(1,2)],
        #     2: [(1,3)]
        # }
        # vis  = {2,3}
        # heap = []
        # time, node = 1,3
        
        # times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
        # adj = {
        #     1: [(1,2), (4,4)],
        #     2: [(1,3)],
        #     3: [(1,4)]
        # }
        # vis  = {1,2,3,4}
        # heap = [
        #     (4,4)
        # ]
        # time, node = 3,4