class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])


        def valid(x: int, y: int) -> bool:
            if x < 0 or x >= ROWS:
                return False
            if y < 0 or y >= COLS:
                return False
            
            return True

        mem = {}
        def dfs(x: int, y: int) -> int:
            if (x, y) in mem:
                return mem[(x, y)]
            
            mem[(x, y)] = 1

            if valid(x - 1, y) and matrix[x - 1][y] > matrix[x][y]:
                mem[(x, y)] = max(mem[(x, y)], 1 + dfs(x - 1, y))
            if valid(x + 1, y) and matrix[x + 1][y] > matrix[x][y]:
                mem[(x, y)] = max(mem[(x, y)], 1 + dfs(x + 1, y))
            if valid(x, y - 1) and matrix[x][y - 1] > matrix[x][y]:
                mem[(x, y)] = max(mem[(x, y)], 1 + dfs(x, y - 1))
            if valid(x, y + 1) and matrix[x][y + 1] > matrix[x][y]:
                mem[(x, y)] = max(mem[(x, y)], 1 + dfs(x, y + 1))
            
            return mem[(x, y)]
        
        mx = 1
        for x, row in enumerate(matrix):
            for y, element in enumerate(row):
                mx = max(mx, dfs(x, y))
        
        return mx