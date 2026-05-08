class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom up approach (memoization)
        # mem = {}
        # def dfs(i: int) -> int:
        #     if i == n:
        #         return 1
        #     elif i > n:
        #         return 0
            
        #     if i in mem:
        #         return mem[i]
            
        #     mem[i] = dfs(i + 2) + dfs(i + 1)
        #     return mem[i]
        
        # return dfs(0)

        # Top down approach:
        mem = {}
        def dfs(i: int) -> int:
            if i < 2 and i >= 0:
                return 1
            elif i < 0:
                return 0
            
            if i in mem:
                return mem[i]
            
            mem[i] = dfs(i - 2) + dfs(i - 1)
            return mem[i]
        
        return dfs(n)

