class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visp = set()
        visa = set()

        gridP = [row[:] for row in heights]
        gridA = [row[:] for row in heights]

        qp = deque()
        qa = deque()

        def addCellP(r: int, c: int, prevHeight: int):
            if (r < 0 or
                ROWS <= r or
                c < 0 or
                COLS <= c or
                (r, c) in visp or
                prevHeight > gridP[r][c]):
                return
            
            qp.append((r, c))
            
        def addCellA(r: int, c: int, prevHeight: int):
            if (r < 0 or
                ROWS <= r or
                c < 0 or
                COLS <= c or
                (r, c) in visa or
                prevHeight > gridA[r][c]):
                return
            
            qa.append((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    qp.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    qa.append((r, c))
        
        print(gridP)
        print(gridA)
        
        print(qp)
        print(qa)

        while qp:
            for i in range(len(qp)):
                r, c = qp.popleft()
                prevHeight = gridP[r][c]
                visp.add((r, c))

                addCellP(r - 1, c, prevHeight)
                addCellP(r + 1, c, prevHeight)
                addCellP(r, c - 1, prevHeight)
                addCellP(r, c + 1, prevHeight)
        
        while qa:
            for i in range(len(qa)):
                r, c = qa.popleft()
                prevHeight = gridA[r][c]
                visa.add((r, c))

                addCellA(r - 1, c, prevHeight)
                addCellA(r + 1, c, prevHeight)
                addCellA(r, c - 1, prevHeight)
                addCellA(r, c + 1, prevHeight)
        
        print(visp)
        print(visa)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visp and (r, c) in visa:
                    res.append([r, c])

        return res