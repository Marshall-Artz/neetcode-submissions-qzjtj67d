class Solution:
    def romanToInt(self, s: str) -> int:
        RtoI = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1:
            return RtoI[s]

        res = 0
        for i in range(len(s) - 1):
            char = s[i]
            nextChar = s[i + 1]

            curInt = RtoI[char]
            nextInt = RtoI[nextChar]
            
            if curInt < nextInt:
                res -= curInt
            else:
                res += curInt

        return res + RtoI[s[-1]]

        # s = "IV"
        # i = 0
        # char, curInt = "I", 1
        # nextChar, nextInt = "V", 5
        # res = -1 + 5

        # s = "XXV II"
        # i = 3
        # char, curInt = "I", 1
        # nextChar, nextInt = "I", 1
        # res = 26 + 1

        # s = "XLI X"
        # i = 2
        # char, curInt = "I", 1
        # nextChar, nextInt = "X", 10
        # res = 39 + 10

        # s = "III"
        # i = 1
        # char, curInt = "I", 1
        # nextChar, nextInt = "I", 1
        # res = 2 + 1