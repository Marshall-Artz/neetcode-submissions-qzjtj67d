class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []

        for numPassengers, frm, to in trips:
            heapq.heappush(heap, (frm, numPassengers))
            heapq.heappush(heap, (to, -numPassengers))
        
        car = 0
        while heap:
            car += heap[0][1]
            heapq.heappop(heap)
            
            if car > capacity:
                return False
        
        return True
