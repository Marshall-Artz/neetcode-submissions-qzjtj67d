class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue  = deque()

        def valid(r: int, c: int) -> bool:
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return False
            else:
                return True
        
        def rotFruit(r: int, c: int) -> None:
            nonlocal fruitCount
            if valid(r, c) and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r, c))
                fruitCount -= 1

        # Populate rotten array and fruitCount
        fruitCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fruitCount += 1
        
        if fruitCount == 0:
            return 0
        
        time = 0
        while queue:
            print("fruitCount", fruitCount)
            for i in range(len(queue)):
                r, c = queue.popleft()
                rotFruit(r - 1, c)
                rotFruit(r + 1, c)
                rotFruit(r, c - 1)
                rotFruit(r, c + 1)
            time += 1
        
        if fruitCount != 0:
            return -1

        return time - 1