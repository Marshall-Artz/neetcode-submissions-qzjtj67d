class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dfs(pos: int) -> int:
            if pos in mem:
                return mem[pos]
            if pos == n:
                return 1
            if pos > n:
                return 0
            
            mem[pos] = dfs(pos + 1) + dfs(pos + 2)

            return mem[pos]
        
        return dfs(0)