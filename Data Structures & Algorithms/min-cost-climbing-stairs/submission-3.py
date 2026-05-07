class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}
        def dfs(pos: int, curCost: int) -> int:
            if pos >= len(cost):
                return curCost

            if (pos, curCost) in mem:
                return mem[(pos, curCost)]
            
            # Step Two or Step One:
            mem[(pos, curCost)] = min(
                dfs(pos + 2, curCost + cost[pos]),
                dfs(pos + 1, curCost + cost[pos])
                )
            return mem[(pos, curCost)]
        
        return min(dfs(0, 0), dfs(1,0))

        # cost    = [1,2, 3]
        # pos     = 4
        # curCost = 4