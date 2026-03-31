class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(pos: int) -> int:
            # Base case:
            if pos in mem:
                return mem[pos]
            if pos >= len(nums):
                return 0
            
            money = nums[pos] if pos >= 0 else 0

            mem[pos] = max(money + dfs(pos + 2), money + dfs(pos + 3))

            return mem[pos]
        
        return dfs(-2)