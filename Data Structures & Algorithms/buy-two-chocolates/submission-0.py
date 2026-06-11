class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)

        sm = 0
        sm += heapq.heappop(prices)
        sm += heapq.heappop(prices)

        return money - sm if sm <= money else money