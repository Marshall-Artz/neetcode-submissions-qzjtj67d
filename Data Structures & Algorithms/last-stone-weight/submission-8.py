class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            stones[i] *= -1

        while len(stones) > 1:
            heapq.heapify(stones)
            first  = heapq.heappop(stones)
            print("stones:", stones)
            print("first:", first)

            if stones[0] == first:
                heapq.heappop(stones)
                continue
            else:
                stones[0] = (max(-first, -stones[0]) - min(-first, -stones[0])) * -1
            print("stones[0]:", stones[0])
        
        if not stones:
            return 0

        return -stones[0]