class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Base Cases:
        # - if i >= len(prices):
        #   - return profit
        # - Check neetcoin count:
        #   - 1:
        #     - Sell:
        #       - add profit
        #       - go to i + 2
        #     - Continue holding
        #   - 0:
        #     - Buy
        #     - Don't buy
        # 
        # return profit
        #
        # def buyOrSell(i: int, neetcoin: int) -> int:

        mem = {}
        def buyOrSell(i: int, neetcoin: int) -> int:
            # Base cases
            if i >= len(prices):
                return 0
            if (i, neetcoin) in mem:
                return mem[(i, neetcoin)]
            if neetcoin:
                # Sell decisions:
                mem[(i, neetcoin)] = max(
                    prices[i] + buyOrSell(i + 2, 0), # Sell
                    buyOrSell(i + 1, 1) # Don't sell
                )
                return mem[(i, neetcoin)]
            
            # Buy decisions:
            mem[(i, neetcoin)] = max(
                -prices[i] + buyOrSell(i + 1, 1), # Buy today
                buyOrSell(i + 1, 0) # Don't buy today
            )
            return mem[(i, neetcoin)]
        
        return buyOrSell(0, 0)