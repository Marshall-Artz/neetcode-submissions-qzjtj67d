class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []

        for numPassengers, frm, to in trips:
            heapq.heappush(heap, (frm, numPassengers))
            heapq.heappush(heap, (to, -numPassengers))
        
        car = 0
        while heap:
            nxt = heap[0][0]

            _, numPassengersEnd = heapq.heappop(heap)
            car += numPassengersEnd
            
            if car > capacity:
                return False
        
        return True
