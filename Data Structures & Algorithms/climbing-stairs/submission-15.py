class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def dfs(n: int) -> int:
            if n in mem:
                return mem[n]
            if n == 0 or n == 1:
                return 1

            mem[n] = dfs(n - 2) + dfs(n - 1)
            return mem[n]
        
        return dfs(n)

        # n = 2
        # dfs(2)
        #     0 + 1