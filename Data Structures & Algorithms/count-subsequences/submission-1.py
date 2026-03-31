class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        mem = {}
        def subs(i: int, j: int) -> int:
            if (i, j) in mem:
                return mem[(i, j)]
            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0
            
            mem[(i, j)] = 0
            if s[i] == t[j]:
                # Include character, or keep looking for another
                mem[(i, j)] += subs(i + 1, j + 1)
            
            mem[(i, j)] += subs(i + 1, j)

            return mem[(i, j)]

        return subs(0, 0)
