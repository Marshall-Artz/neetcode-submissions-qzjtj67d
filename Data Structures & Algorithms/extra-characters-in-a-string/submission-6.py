class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = {}

        for word in dictionary:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = True
        
        memo = {}

        def dfs(pos: int) -> int:
            if pos >= len(s):
                return 0
            if pos in memo:
                return memo[pos]

            # Option 1: Current character is an extra character
            res = dfs(pos + 1)

            # Option 2: Try to match words starting at pos using the Trie
            curr_node = trie
            for i in range(pos, len(s)):
                if s[i] not in curr_node:
                    break
                curr_node = curr_node[s[i]]
                if '#' in curr_node:
                    # If a word is formed, add its length and recurse
                    res = max(res, (i - pos + 1) + dfs(i + 1))
            
            memo[pos] = res
            return res

        return len(s) - dfs(0)