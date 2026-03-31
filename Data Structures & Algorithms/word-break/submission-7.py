class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Decision Tree:
        # - Split cur char
        # - Include current char

        self.trie = {}

        for word in wordDict:
            cur = self.trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = True
        
        mem = {}
        def dfs(pos: int, cur: dict) -> bool:
            state = (pos, id(cur))
            if state in mem:
                return mem[state]
            if pos >= len(s):
                return '#' in cur
            
            mem[state] = False
            if s[pos] in cur and dfs(pos + 1, cur[s[pos]]):
                mem[state] = True
                return True
            if '#' in cur and dfs(pos, self.trie):
                mem[state] = True
                return True

            return False

        return dfs(0, self.trie)
