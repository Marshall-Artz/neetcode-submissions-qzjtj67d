class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1

        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        
        return profit

        # prices = [10,8,7,5,2]
        # l, prices[l] = 4, 2
        # r, prices[r] = 5, 2
        # profit = 0

        # prices = [10,1,5,6,7,1]
        # l, prices[l] = 1, 1
        # r, prices[r] = 5, 1
        # profit = 6