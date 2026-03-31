class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exists(i: int, j: int) -> bool:
            if i < 0 or j < 0:
                return False
            if i >= len(board) or j >= len(board[0]):
                return False
            
            return True

        s = set()
        def dfs(i: int, j: int, x: int):
            if not exists(i, j):
                return False
            if (i, j) in s:
                return False
            if x == len(word) - 1 and board[i][j] == word[x]:
                return True
            if board[i][j] != word[x]:
                return False
            
            s.add((i, j))
            
            b = dfs(i, j - 1, x + 1) or dfs(i, j + 1, x + 1) or dfs(i - 1, j, x + 1) or dfs(i + 1, j, x + 1)

            s.remove((i, j))

            return b

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    print("calling dfs for:", board[i][j])
                    if dfs(i, j, 0):
                        return True
        
        return False