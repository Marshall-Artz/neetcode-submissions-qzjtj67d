class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def getDigit(c: str) -> int:
            if   c == "0": return 0
            elif c == "1": return 1
            elif c == "2": return 2
            elif c == "3": return 3
            elif c == "4": return 4
            elif c == "5": return 5
            elif c == "6": return 6
            elif c == "7": return 7
            elif c == "8": return 8
            elif c == "9": return 9
        
        def getChar(i: int) -> str:
            if   i == 0: return "0"
            elif i == 1: return "1"
            elif i == 2: return "2"
            elif i == 3: return "3"
            elif i == 4: return "4"
            elif i == 5: return "5"
            elif i == 6: return "6"
            elif i == 7: return "7"
            elif i == 8: return "8"
            elif i == 9: return "9"
        
        newN1 = 0
        for i in range(len(num1)):
            newN1 = (newN1 * 10) + getDigit(num1[i])
        
        newN2 = 0
        for i in range(len(num2)):
            newN2 = (newN2 * 10) + getDigit(num2[i])
        
        product = newN1 * newN2

        if product == 0:
            return "0"

        res = ""
        while product:
            res = getChar(product % 10) + res
            product = product // 10
        
        return res

