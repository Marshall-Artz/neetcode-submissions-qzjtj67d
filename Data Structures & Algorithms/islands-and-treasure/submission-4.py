class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def valid(r: int, c: int) -> bool:
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return False
            if grid[r][c] == pow(2, 31) - 1:
                return True
            return False
        
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        
        while queue:
            for i in range(len(queue)):
                row, col, dist = queue.popleft()
                dist += 1
                if valid(row - 1, col):
                    grid[row - 1][col] = dist
                    queue.append((row - 1, col, dist))
                if valid(row + 1, col):
                    grid[row + 1][col] = dist
                    queue.append((row + 1, col, dist))
                if valid(row, col - 1):
                    grid[row][col - 1] = dist
                    queue.append((row, col - 1, dist))
                if valid(row, col + 1):
                    grid[row][col + 1] = dist
                    queue.append((row, col + 1, dist))
                
        
        return None