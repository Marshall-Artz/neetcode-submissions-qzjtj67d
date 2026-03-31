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
            
            first_match = True if i < len(s) and (s[i] == p[j] or p[j] == '.') else False

            mem[(i, j)] = False
            if j + 1 < len(p) and p[j + 1] == '*':
                mem[(i, j)] = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                mem[(i, j)] = first_match and dfs(i + 1, j + 1)
            
            return mem[(i, j)]
        
        return dfs(0, 0)