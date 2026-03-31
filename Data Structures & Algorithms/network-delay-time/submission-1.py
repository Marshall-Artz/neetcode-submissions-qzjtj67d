class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for node, target, weight in times:
            edges[node].append((target, weight))
        
        visit = set()
        heap  = [(0, k)]
        t     = 0

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            t = max(t, w1)

            visit.add(n1)

            for target, weight in edges[n1]:
                if target not in visit:
                    heapq.heappush(heap, (w1 + weight, target))
        
        return t if len(visit) == n else -1
