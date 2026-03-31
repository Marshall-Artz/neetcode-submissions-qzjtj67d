class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        val = 1

        while n:
            val = (n & 1)
            res += val
            n = n >> 1

        return res