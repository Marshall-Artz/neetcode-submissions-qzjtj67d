class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxRight = [0]
        revPrices = prices[::-1]

        for i in range(1, len(revPrices)):
            movingMax = max(maxRight[-1], revPrices[i - 1])
            maxRight.append(movingMax)
        
        maxRight = maxRight[::-1]

        maxSale = maxRight[-1]
        for i in range(len(prices)):
            maxSale = max(maxSale, (maxRight[i] - prices[i]))

        return maxSale