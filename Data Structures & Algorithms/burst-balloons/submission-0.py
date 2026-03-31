class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        mem = {}
        def dfs(l: int, r: int) -> int:
            if (l, r) in mem:
                return mem[(l, r)]
            if l > r:
                return 0
            
            mem[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                mem[(l, r)] = max(coins, mem[(l, r)])
            return mem[(l, r)]
        
        return dfs(1, len(nums) - 2)