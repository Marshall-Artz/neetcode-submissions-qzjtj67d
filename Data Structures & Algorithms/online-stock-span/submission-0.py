class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        newCount = 1
        while self.prices and self.prices[-1][0] <= price:
            val, count = self.prices.pop()
            newCount += count
        self.prices.append((price, newCount))
        return self.prices[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)