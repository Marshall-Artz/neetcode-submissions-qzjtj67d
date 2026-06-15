class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = 0
        ones  = 0

        for char in s:
            if char == '0':
                zeros += 1
            elif char == '1':
                ones += 1
        
        ones -=  1
        res   = "1"

        while zeros or ones:
            if zeros:
                res = res + "0"
                zeros -= 1
            else:
                res = res + "1"
                ones -= 1

        return res[::-1]

        # s     = "100"
        # zeros = 0
        # ones  = 0
        # res   = "100"
        # res[::-1] = "001"

        # s     = "0110"
        # zeros = 0
        # ones  = 0
        # res   = "1001"
