class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(num):
            if num in mem:
                return mem[num]
            
            if num == n:
                return 1
            if num > n:
                return 0

            mem[num] = dfs(num + 1) + dfs(num + 2)

            return mem[num]
        
        return dfs(0)