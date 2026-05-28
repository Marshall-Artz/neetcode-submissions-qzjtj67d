class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def valid(i: int, j: int) -> bool:
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0])):
                return False
            
            return True

        vis  = set()
        heap = [(grid[0][0], 0, 0)]
        time = 0

        while heap:
            elv, x, y = heapq.heappop(heap)

            if (x, y) in vis:
                continue
            
            vis.add((x,y))

            if time <= elv:
                time = elv

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return time

            if valid(x - 1, y) and (x - 1, y) not in vis:
                heapq.heappush(heap, (grid[x - 1][y], x - 1, y))
            if valid(x + 1, y) and (x + 1, y) not in vis:
                heapq.heappush(heap, (grid[x + 1][y], x + 1, y))
            if valid(x, y - 1) and (x, y - 1) not in vis:
                heapq.heappush(heap, (grid[x][y - 1], x, y - 1))
            if valid(x, y + 1) and (x, y + 1) not in vis:
                heapq.heappush(heap, (grid[x][y + 1], x, y + 1))
        
        return -1
            
        
        # vis  = {(0,0), (0,1), (0,2), (1,2), (2,2), (6,6)}
        # heap = [(7,3,2), (9,1,0), (10,0,3), (13,3,1), (14,1,1), (14,1,1)]
        # time = 8
        # elv, x, y = 6,3,3