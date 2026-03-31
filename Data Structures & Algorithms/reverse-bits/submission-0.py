class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(1, 33):
            res += (n & 1) * pow(2, (32 - i))
            n = n >> 1
        
        return res