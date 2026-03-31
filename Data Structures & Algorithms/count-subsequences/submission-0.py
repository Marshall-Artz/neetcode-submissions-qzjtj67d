class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def subs(i: int, j: int) -> int:
            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0
            
            res = 0
            if s[i] == t[j]:
                # Include character, or keep looking for another
                res += subs(i + 1, j + 1)
            
            res += subs(i + 1, j)

            return res

        return subs(0, 0)
