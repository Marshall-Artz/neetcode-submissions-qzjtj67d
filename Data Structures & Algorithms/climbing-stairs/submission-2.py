class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        mem = {}

        def dfs(num, res):
            if num in mem:
                return mem[num]
            
            if num == n:
                res += 1
            if num > n:
                return 0

            d1 = dfs(num + 1, res)
            d2 = dfs(num + 2, res)

            mem[num + 1] = d1
            mem[num + 2] = d2

            return d1 + d2 + res
        
        return dfs(0, 0)