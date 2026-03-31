class Solution:
    def countSubstrings(self, s: str) -> int:

        def dfs(i: int) -> int:
            res = 0
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s):
                pali = s[l:r]
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                pali = s[l:r]
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1
            
            return res
        
        res = 0
        for i in range(len(s)):
            res += dfs(i)
        
        return res