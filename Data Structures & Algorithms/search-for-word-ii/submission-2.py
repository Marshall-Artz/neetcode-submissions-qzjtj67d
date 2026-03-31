class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = {}
        res = []

        # Load trie of words
        for word in words:
            cur = self.trie
            for char in word:
                # Create branch if it doesn't exist
                if char not in cur:
                    cur[char] = {}
                # Continue going down that branch
                cur = cur[char]
            cur['#'] = True
        
        def exists(r: int, c: int) -> bool:
            if r < 0 or r >= len(board):
                return False
            if c < 0 or c >= len(board[0]):
                return False
            
            return True
        
        def dfs(cur: dict, word: str, r: int, c: int) -> str:
            if not exists(r, c) or board[r][c] not in cur or board[r][c] == '.':
                return
            
            char = board[r][c]
            next_node = cur[char]

            if '#' in next_node:
                res.append(word + char)
                del next_node['#']

            board[r][c] = '.'

            dfs(next_node, word + char, r - 1, c)
            dfs(next_node, word + char, r + 1, c)
            dfs(next_node, word + char, r, c - 1)
            dfs(next_node, word + char, r, c + 1)

            board[r][c] = char

            if not next_node:
                del cur[char]
        
        for r, row in enumerate(board):
            for c, char in enumerate(row):
                dfs(self.trie, "", r, c)
        
        return res