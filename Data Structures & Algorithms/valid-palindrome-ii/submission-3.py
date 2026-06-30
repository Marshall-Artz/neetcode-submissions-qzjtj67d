class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = ""
        if len(s) <= 1:
            return True
        for i in range(len(s) // 2):
            inv = len(s) - i - 1

            if s[i] != s[inv]:
                s1 = s[:i] + s[i + 1:]
                s2 = s[:inv] + s[inv + 1:]

                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
            
        return True