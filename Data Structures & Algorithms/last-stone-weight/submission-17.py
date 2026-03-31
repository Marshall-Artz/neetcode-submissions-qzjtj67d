class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            heapq.heappush(stones, (heapq.heappop(stones) - heapq.heappop(stones)))
        
        if not stones:
            return 0

        return -stones[0]