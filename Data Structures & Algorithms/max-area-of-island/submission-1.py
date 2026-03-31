class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def valid(r: int, c: int) -> bool:
            numRows = len(grid)
            numCols = len(grid[0])
            if r < 0 or r >= numRows:
                return False
            if c < 0 or c >= numCols:
                return False
            if grid[r][c] == 0:
                return False

            return True
        
        def dfs(r: int, c: int) -> int:
            res = 1
            grid[r][c] = 0

            if valid(r - 1, c): res += dfs(r - 1, c)
            if valid(r + 1, c): res += dfs(r + 1, c)
            if valid(r, c - 1): res += dfs(r, c - 1)
            if valid(r, c + 1): res += dfs(r, c + 1)

            return res

        mx = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if valid(r, c):
                    mx = max(mx, dfs(r, c))

        return mx