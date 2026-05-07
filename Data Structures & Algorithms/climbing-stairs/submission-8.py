class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = {}
        def dfs(pos: int) -> int:
            if pos == n:
                return 1
            elif pos > n:
                return 0
            
            if pos in mem:
                return mem[pos]

            mem[pos] = dfs(pos + 2) + dfs(pos + 1)
            return mem[pos]
        
        return dfs(0)