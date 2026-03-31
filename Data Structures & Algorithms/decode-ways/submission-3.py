class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        count = 0

        def dfs(pos: int):
            nonlocal count
            if pos >= len(s):
                count += 1
                return
            if s[pos] == "0":
                return
            
            dfs(pos + 1)

            if pos + 1 < len(s) and int(s[pos:pos+2]) <= 26:
                dfs(pos + 2)

        dfs(0)
        return count