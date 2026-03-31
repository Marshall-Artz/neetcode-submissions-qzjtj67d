class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        
        return True