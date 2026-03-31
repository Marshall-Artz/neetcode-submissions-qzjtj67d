class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Two values:
        # - bit value
        # - carry value
        mask = 0xFFFFFFFF
        if b == 0:
            return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        if a == 0:
            return b if b <= 0x7FFFFFFF else ~(b ^ mask)
        
        bit   = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        
        return self.getSum(bit, carry)