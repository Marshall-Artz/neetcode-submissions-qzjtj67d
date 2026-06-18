class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        heapq.heapify(intervals)
        heap = intervals
        heapq.heappush(heap, newInterval)

        res = [heapq.heappop(heap)]

        while heap:
            topStart, topEnd = res[-1][0], res[-1][1]
            botStart, botEnd = heap[0][0], heap[0][1]

            # Non-Overlap:
            if topEnd < botStart:
                res.append(heapq.heappop(heap))
            else: # Overlap:
                res[-1][0], res[-1][1] = min(topStart, botStart), max(topEnd, botEnd)
                heapq.heappop(heap)
        
        return res

        # intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        # heap = []
        # res  = [[1,2],[3,5],[6,7],[9,10]]
        # topStart, topEnd = 6, 7
        # botStart, botEnd = 9, 10

        # intervals = [[1,3],[4,6]], newInterval = [2,5]
        # heap = []
        # res  = [[1,6]]
        # topStart, topEnd = 1, 5
        # botStart, botEnd = 4, 6