class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            temp = a
            a = (a ^ b) & mask
            b = (temp & b) << 1

        return a if a <= 0x7fffffff else ~(a ^ mask)