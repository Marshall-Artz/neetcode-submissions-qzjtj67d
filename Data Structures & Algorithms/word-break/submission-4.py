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
        
        memo = {}
        def dfs(pos: int, cur: dict) -> bool:
            state = (pos, id(cur))
            if state in memo: return memo[state]
            
            if pos >= len(s):
                return '#' in cur
            
            res = False
            if s[pos] in cur and dfs(pos + 1, cur[s[pos]]): res = True
            elif '#' in cur and dfs(pos, self.trie): res = True

            memo[state] = res
            return res

        return dfs(0, self.trie)