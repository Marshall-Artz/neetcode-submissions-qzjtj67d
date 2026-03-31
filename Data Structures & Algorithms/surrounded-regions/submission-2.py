class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        edge = set()
        q = deque()

        def addCell(r: int, c: int):
            if (r < 0 or ROWS <= r or
                c < 0 or COLS <= c):
                return
            if board[r][c] == "O" and (r, c) not in edge:
                edge.add((r, c))
                q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1) and
                    board[r][c] == "O"):
                    q.append((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                edge.add((r, c))

                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)

        print("old board:")
        for r in range(ROWS):
            print(board[r])
        print()
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in edge:
                    board[r][c] = "X"
        
        for r in range(ROWS):
            print(board[r])