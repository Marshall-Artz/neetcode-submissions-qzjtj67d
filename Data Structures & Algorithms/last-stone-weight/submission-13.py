class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            first  = heapq.heappop(stones)
            second = heapq.heappop(stones)
            first = min(first, second) - max(first, second)
            heapq.heappush(stones, first)
        
        if not stones:
            return 0

        return -first