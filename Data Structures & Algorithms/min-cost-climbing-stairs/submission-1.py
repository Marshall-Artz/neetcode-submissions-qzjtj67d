class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}

        def dfs(pos: int) -> int:
            # Base cases:
            if pos in mem:
                return mem[pos]
            if pos >= len(cost):
                return 0

            # Calculate cost
            c = cost[pos] if pos >= 0 else 0

            # Store the recursive result of dfs:
            mem[pos] = min(c + dfs(pos + 1), c + dfs(pos + 2))

            # Return min result
            return mem[pos]
        
        return dfs(-1)