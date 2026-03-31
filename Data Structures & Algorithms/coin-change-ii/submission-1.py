class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Base cases:
        # - if val == amount:
        #   - return 1
        # - if val > amount:
        #   - return 0
        # Decision:
        # - Use coin[i]
        # - Use coin[i + 1]
        #
        # def coinCombos(value: int) -> int:

        if amount == 0:
            return 1
        
        mem = {}
        def coinChange(val: int, coinIndex: int) -> int:
            if (val, coinIndex) in mem:
                return mem[(val, coinIndex)]
            if val == 0:
                return 1
            if val < 0:
                return 0
            if coinIndex >= len(coins):
                return 0
            
            mem[(val, coinIndex)] = (
                coinChange(val - coins[coinIndex], coinIndex) +
                coinChange(val, coinIndex + 1)
            )

            return mem[(val, coinIndex)]
        
        return coinChange(amount, 0)