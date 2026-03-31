class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        def valid(r: int, c: int) -> bool:
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return False
            if grid[r][c] == pow(2, 31) - 1:
                return True
            return False
        
        def addRoom(r: int, c: int, next_dist: int):
            if valid(r, c):
                grid[r][c] = next_dist
                queue.append((r, c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                addRoom(row - 1, col, dist + 1)
                addRoom(row + 1, col, dist + 1)
                addRoom(row, col - 1, dist + 1)
                addRoom(row, col + 1, dist + 1)
            dist += 1
        
        return None