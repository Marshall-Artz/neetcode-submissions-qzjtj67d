class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        res = 0
        
        def dfs(x: int, y: int) -> int:
            # base cases
            if x >= m or y >= n:
                return 0
            if x == m - 1 and y == n - 1:
                return 1

            count = 0

            # Down right path
            count += dfs(x + 1, y)

            # Down bottom path
            count += dfs(x, y + 1)

            return count
        
        return dfs(0, 0)