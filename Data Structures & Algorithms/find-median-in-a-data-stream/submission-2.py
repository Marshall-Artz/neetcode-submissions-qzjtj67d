class MedianFinder:

    def __init__(self):
        self.upper = []
        self.lower = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if (len(self.lower) + len(self.upper)) % 2 == 0:
            return float((-self.lower[0] + self.upper[0]) / 2.0)
        else:
            return float(-self.lower[0])