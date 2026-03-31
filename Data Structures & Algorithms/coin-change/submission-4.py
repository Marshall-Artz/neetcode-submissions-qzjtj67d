class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if len(coins) == 1 and amount % coins[0] == 0:
            return int(amount / coins[0])
        elif len(coins) == 1 and amount % coins[0] != 0:
            return -1

        mem = {}

        def dfs(total: int) -> int:
            if total in mem:
                return mem[total]
            if total == amount:
                return 0
            if total > amount:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(total + coin))
            
            mem[total] = res
            return res
        
        ans = dfs(0)
        return ans if ans != float('inf') else -1