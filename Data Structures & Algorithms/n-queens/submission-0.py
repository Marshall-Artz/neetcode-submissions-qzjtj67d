class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Result will be a list of strings where each string is each row
        #   and each . is empty, each Q is a square with a Q
        res = []

        def isValid(board: list, row: int, col: int) -> bool:
            queens = set()

            for r, curRow in enumerate(board):
                for c, curCol in enumerate(curRow):
                    if board[r][c] == 'Q':
                        if c == col:
                            return False
                        if r + c == row + col:
                            return False
                        if r - c == row - col:
                            return False
            
            return True

        board = []
        def dfs(i: int):
            # Base case for appending each string:
            if len(board) >= n:
                res.append(board.copy())
                return
            
            # Loop through each square and each Queen possibility:
            #   For each row there will 1 Queen and n possibilities to check
            #   Hard part: How to check if next row is invalid and skip it?
            #      (shared column: easy) (diagonal: difficult, helper function?)
            row = "." * n
            for i in range(n):
                rowToCheck = row[:i] + 'Q' + row[i+1:]
                if isValid(board, len(board), i):
                    board.append(rowToCheck)
                    dfs(i + 1)
                    board.pop()

        
        dfs(0)
        return res