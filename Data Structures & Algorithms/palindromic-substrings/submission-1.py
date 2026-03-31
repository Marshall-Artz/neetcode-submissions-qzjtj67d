class Solution:
    def countSubstrings(self, s: str) -> int:
        seen = set()
        def dfs(i: int, j: int) -> int:
            if i < 0 or j >= len(s) or i > j or (i, j) in seen:
                return 0
            seen.add((i, j))
            res = 0
            st  = s[i:j + 1]
            if st != "" and st == st[::-1]:
                res += 1
        
            res += dfs(i + 1, j)
            res += dfs(i, j - 1)

            return res

        return dfs(0, len(s) - 1)