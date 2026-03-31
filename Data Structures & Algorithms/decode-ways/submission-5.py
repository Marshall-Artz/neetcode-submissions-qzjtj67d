class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}

        def dfs(pos: int):
            if pos in mem:
                return mem[pos]
            if pos >= len(s):
                return 1
            if s[pos] == "0":
                return 0
            
            choice1 = dfs(pos + 1)
            choice2 = dfs(pos + 2) if pos + 1 < len(s) and int(s[pos:pos+2]) <= 26 else 0
            
            mem[pos] = choice1 + choice2

            return mem[pos]

        return dfs(0)