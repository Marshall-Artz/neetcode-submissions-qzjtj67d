class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if i < len(s) and j >= len(p):
                return False
            
            first_match = True if i < len(s) and (s[i] == p[j] or p[j] == '.') else False

            res = False
            if j + 1 < len(p) and p[j + 1] == '*':
                res = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                res = first_match and dfs(i + 1, j + 1)
            
            return res
        
        return dfs(0, 0)