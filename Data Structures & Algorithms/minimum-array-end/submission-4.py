class Solution:
    def minEnd(self, n: int, x: int) -> int:

        n   = n - 1
        res = x
        i   = 0
        while n > 0:
            cur = 1 << i
            if (cur | x) != x:
                if n & 1 == 1:
                    res = res | cur
                n = n >> 1
            i += 1
            

        return res