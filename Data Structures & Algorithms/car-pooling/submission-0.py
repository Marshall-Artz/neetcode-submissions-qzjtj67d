class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minStartHeap = []
        minEndHeap   = []

        for numPassengers, frm, to in trips:
            heapq.heappush(minStartHeap, (frm, numPassengers))
            heapq.heappush(minEndHeap, (to, numPassengers))
        
        car = 0
        while minStartHeap or minEndHeap:
            nextEnd = minEndHeap[0][0] if minEndHeap else float('inf')
            nextStart = minStartHeap[0][0] if minStartHeap else float('inf')

            if nextEnd <= nextStart:
                _, numPassengersEnd = heapq.heappop(minEndHeap)
                car -= numPassengersEnd
            else:
                _, numPassengersStart = heapq.heappop(minStartHeap)
                car += numPassengersStart
            
            if car > capacity:
                return False
        
        return True

        # trips = [[2,1,3],[3,2,4]]
        # capacity     = 4
        # car          = 5
        # minEndHeap   = [(3,2), (4,3)]
        # minStartHeap = []
        # nextEnd, numPassengersEnd     = 3, 2
        # nextStart, numPassengersStart = 2, 3

        # trips = [[4,1,2], [3,2,4]]
        # capacity     = 4
        # car          = 3
        # minEndHeap   = [ (4,3)]
        # minStartHeap = [ ]
        # nextEnd, numPassengersEnd     = 4, 3 #
        # nextStart, numPassengersStart = 2, 3
