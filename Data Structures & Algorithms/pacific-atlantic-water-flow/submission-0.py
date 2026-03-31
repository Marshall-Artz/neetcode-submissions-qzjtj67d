class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])

        def isPacific(r: int, c: int) -> bool:
            return r < 0 or c < 0

        def isAtlantic(r: int, c: int) -> bool:
            return r >= ROWS or c >= COLS
        
        def searchP(r: int, c: int, prev_height: int) -> bool:
            if isPacific(r, c):
                return True
            if isAtlantic(r, c) or (r, c) in visited or heights[r][c] > prev_height:
                return False
            return dfsP(r, c)
        
        def searchA(r: int, c: int, prev_height: int) -> bool:
            if isAtlantic(r, c):
                return True
            if isPacific(r, c) or (r, c) in visited or heights[r][c] > prev_height:
                return False
            return dfsA(r, c)
        
        def dfsP(r: int, c: int) -> bool:
            visited.add((r, c))
            h = heights[r][c]
            if (searchP(r - 1, c, h) or
                searchP(r + 1, c, h) or
                searchP(r, c - 1, h) or
                searchP(r, c + 1, h)):
                return True
            return False
        
        def dfsA(r: int, c: int) -> bool:
            visited.add((r, c))
            h = heights[r][c]
            if (searchA(r - 1, c, h) or
                searchA(r + 1, c, h) or
                searchA(r, c - 1, h) or
                searchA(r, c + 1, h)):
                return True
            return False
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                pacific = dfsP(r, c)
                visited = set()
                atlantic = dfsA(r, c)
                if pacific and atlantic:
                    res.append([r, c])
        
        return res