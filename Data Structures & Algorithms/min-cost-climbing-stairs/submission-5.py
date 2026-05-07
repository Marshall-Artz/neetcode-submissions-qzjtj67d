class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}
        def dfs(pos: int) -> int:
            if pos >= len(cost):
                return 0
            if pos in mem:
                return mem[pos]
            
            mem[pos] = cost[pos] + min(dfs(pos + 1), dfs(pos + 2))
            print(mem)
            return mem[pos]
        
        return min(dfs(0), dfs(1))