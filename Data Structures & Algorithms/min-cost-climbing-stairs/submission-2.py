class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def dfs(pos: int) -> int:
            # Base cases:
            if pos in mem:
                return mem[pos]
            if pos >= len(cost):
                return 0

            # Store the recursive result of dfs:
            mem[pos] = min(cost[pos] + dfs(pos + 1), cost[pos] + dfs(pos + 2))

            # Return min result
            return mem[pos]
        
        return min(dfs(0), dfs(1))