class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []

        # Store original indices for each query to handle duplicates correctly
        qMap = defaultdict(list)
        for idx, query in enumerate(queries):
            qMap[query].append(idx)

        sorted_queries = sorted(list(qMap.keys()))
        res = {}
        
        i = 0
        for query in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(minHeap, (length, right))
                i += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            res[query] = minHeap[0][0] if minHeap else -1

        return [res[query] for query in queries]
