class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def valid(i: int, j: int) -> bool:
            if ((i < 0 or i >= len(grid)) or
                (j < 0 or j >= len(grid[0]))):
                return False
            
            return True
        
        def isWater(i: int, j: int) -> bool:
            if grid[i][j] == 0:
                return True
            return False
        
        visited = set()
        def dfs(i: int, j: int) -> int:
            if ((i, j) in visited or
                grid[i][j] == 0):
                return 0
            
            visited.add((i, j))

            res = 0

            res += 1 if not valid(i - 1, j) or isWater(i - 1, j) else dfs(i - 1, j)
            res += 1 if not valid(i + 1, j) or isWater(i + 1, j) else dfs(i + 1, j)
            res += 1 if not valid(i, j - 1) or isWater(i, j - 1) else dfs(i, j - 1)
            res += 1 if not valid(i, j + 1) or isWater(i, j + 1) else dfs(i, j + 1)

            return res
        
        res = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                res += dfs(i, j)
        
        return res