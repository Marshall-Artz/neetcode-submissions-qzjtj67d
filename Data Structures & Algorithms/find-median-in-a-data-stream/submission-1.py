class MedianFinder:

    def __init__(self):
        self.heaplower = []
        self.heapupper = []

    def addNum(self, num: int) -> None:
        # Push to max-heap, then move the largest of max-heap to min-heap to maintain order
        heapq.heappush(self.heaplower, -num)
        heapq.heappush(self.heapupper, -heapq.heappop(self.heaplower))
        
        # Maintain balance: heaplower can have at most one more element than heapupper
        if len(self.heapupper) > len(self.heaplower):
            heapq.heappush(self.heaplower, -heapq.heappop(self.heapupper))

    def findMedian(self) -> float:
        if len(self.heaplower) > len(self.heapupper):
            return float(-self.heaplower[0])
        else:
            return float((-self.heaplower[0] + (self.heapupper[0])) / 2.0)