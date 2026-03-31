class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        
        for char in s:
            if char.isalpha() or char.isnumeric():
                newStr += char.lower()

        if newStr == newStr[::-1]:
            return True
        else:
            return False