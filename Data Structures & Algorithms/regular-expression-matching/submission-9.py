class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        mem = {}
        def dfs(i: int, j: int) -> bool:
            if (i, j) in mem:
                return mem[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if i < len(s) and j >= len(p):
                return False
            
            mem[(i, j)] = True if i < len(s) and (p[j] == '.' or p[j] == s[i]) else False

            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Skip the '*' and its preceding char (match 0 times)
                # Option 2: Use the '*' (if it matches) and stay at current p index
                res = dfs(i, j + 2) or (mem[(i, j)] and dfs(i + 1, j))
            else:
                res = mem[(i, j)] and dfs(i + 1, j + 1)
            
            mem[(i, j)] = res
            return res
        
        return dfs(0, 0)