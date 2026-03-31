class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        l, r = 0, 0
        
        # Odd loop check:
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substr = s[l:r + 1]
                if len(substr) >= len(res):
                    res = substr
                l -= 1
                r += 1
    
        # Even loop check:
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substr = s[l:r + 1]
                if len(substr) >= len(res):
                    res = substr
                l -= 1
                r += 1

        return res