class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        def addLand(r: int, c: int, dist) -> None:
            if valid(r, c):
                grid[r][c] = dist
                queue.append((r, c))

        def valid(r: int, c: int) -> bool:
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return False
            if grid[r][c] == pow(2, 31) - 1:
                return True
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist

                addLand(row - 1, col, dist + 1)
                addLand(row + 1, col, dist + 1)
                addLand(row, col - 1, dist + 1)
                addLand(row, col + 1, dist + 1)
            dist += 1
                
        
        return None