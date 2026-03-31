class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for source, target, time in times:
            edges[source].append((time, target))
        
        visited = set()
        heap    = [(0, k)]
        time    = 0

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            time = max(time, w1)

            visited.add(n1)

            for w2, n2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))
        
        return time if len(visited) == n else -1
            