class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inbounds(i: int, j: int) -> bool:
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0])):
                return False
            
            return True
        
        def dfs(i: int, j: int) -> int:
            if (not inbounds(i, j) or
                grid[i][j] == "0"):
                return 0
            
            grid[i][j] = "0"

            # Up:
            if inbounds(i - 1, j) and grid[i - 1][j] == "1":
                dfs(i - 1, j)

            # Down:
            if inbounds(i + 1, j) and grid[i + 1][j] == "1":
                dfs(i + 1, j)

            # Left:
            if inbounds(i, j - 1) and grid[i][j - 1] == "1":
                dfs(i, j - 1)

            # Right:
            if inbounds(i, j + 1) and grid[i][j + 1] == "1":
                dfs(i, j + 1)

            return 1
        
        res = 0
        for i, row in enumerate(grid):
            for j, column in enumerate(grid[0]):
                res += dfs(i, j)
        
        return res

        # grid = [
        #     [ "0","1","1","1","0"],
        #     ["0","1","0","1","0"],
        #     ["1","1","0","0","0"],
        #     ["0","0","0","0","0"]
        # ]
        # res = 0