class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom Up (memoization):
        mem = {}
        def dfs(i: int) -> int:
            if i >= len(cost):
                return 0
            
            if i in mem:
                return mem[i]
            
            # Return min of two steps or one step:
            mem[i] = min(
                cost[i] + dfs(i + 2),
                cost[i] + dfs(i + 1)
            )
            return mem[i]
        
        return min(dfs(0), dfs(1))