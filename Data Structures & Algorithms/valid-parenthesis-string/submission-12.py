class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0

        for char in s:
            if char == "(":
                maxLeft += 1
                minLeft += 1
            elif char == ")":
                maxLeft -= 1
                minLeft -= 1
            elif char == "*":
                maxLeft += 1
                minLeft -= 1
            
            if maxLeft < 0:
                return False
            if minLeft < 0:
                minLeft = 0
        
        return minLeft == 0