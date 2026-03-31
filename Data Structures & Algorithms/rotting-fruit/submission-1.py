class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue  = deque()

        def valid(r: int, c: int) -> bool:
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return False
            else:
                return True
        
        def rotFruit(r: int, c: int) -> int:
            if valid(r, c) and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r, c))
                return 1
            return 0

        # Populate rotten array and fruitCount
        fruitCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] != 0:
                    fruitCount += 1
        
        if fruitCount == 0:
            return 0
        
        rotCount = len(queue)
        time = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rotCount += rotFruit(r - 1, c)
                rotCount += rotFruit(r + 1, c)
                rotCount += rotFruit(r, c - 1)
                rotCount += rotFruit(r, c + 1)
            time += 1
        
        if rotCount != fruitCount:
            return -1

        return time - 1