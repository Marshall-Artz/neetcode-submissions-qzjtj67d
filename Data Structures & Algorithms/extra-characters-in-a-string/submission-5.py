class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dic = set()
        for word in dictionary:
            dic.add(word)

        mem = {}
        def dfs(pos: int) -> int:
            if pos in mem:
                return mem[pos]
            if pos >= len(s):
                return 0
            
            res = len(s)
            
            for i in range(len(s)):
                if s[pos:i + 1] in dic:
                    res = min(res, dfs(i + 1))

            mem[pos] = min(res, 1 + dfs(pos + 1))
            
            return mem[pos]
        
        return dfs(0)