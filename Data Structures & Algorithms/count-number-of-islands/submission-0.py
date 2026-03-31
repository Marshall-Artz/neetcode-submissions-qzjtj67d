class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(r: int, c: int):
            if r < 0 or len(grid) <= r:
                return
            if c < 0 or len(grid[0]) <= c:
                return
            if grid[r][c] != "1":
                return
            
            grid[r][c] = '.'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1":
                    dfs(r, c)
                    count += 1
        
        return count