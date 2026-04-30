class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 0:
            return 0

        def countEdge(i: int, j: int) -> bool:
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == 0):
                return True
            
            return False
        
        vis = set()
        def dfs(i: int, j: int) -> int:
            if (grid[i][j] == 0 or
                (i, j) in vis):
                return 0

            count = 0
            vis.add((i, j))
            
            # Side Up:
            if countEdge(i - 1, j):
                count += 1
            else:
                count += dfs(i - 1, j)

            # Side Down
            if countEdge(i + 1, j):
                count += 1
            else:
                count += dfs(i + 1, j)

            # Side Left:
            if countEdge(i, j - 1):
                count += 1
            else:
                count += dfs(i, j - 1)

            # Side Right:
            if countEdge(i, j + 1):
                count += 1
            else:
                count += dfs(i, j + 1)

            return count
        
        res = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                res += dfs(i, j)
        
        return res
        
        # grid = 
        # [[1, 1,0,0],
        #  [1,0,0,0],
        #  [1,1,1,0],
        #  [0,0,1,1]]

        # res = 0

        # count = 3
        # vis = {
        #     (0, 0)
        # }

        