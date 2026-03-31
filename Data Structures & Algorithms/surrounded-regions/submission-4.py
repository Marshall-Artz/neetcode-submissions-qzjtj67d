class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        edge = set()
        queue = deque()

        def addCell(r: int, c: int):
            if (r < 0 or ROWS <= r or
                c < 0 or COLS <= c or
                (r, c) in edge or
                board[r][c] == "X"):
                return
            
            queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1):
                    if board[r][c] == "O": queue.append((r, c))
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                edge.add((r, c))

                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in edge:
                    board[r][c] = "X"