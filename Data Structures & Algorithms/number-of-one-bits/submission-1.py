class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        val = 1

        for i in range(32):
            x = n & val
            if x != 0:
                res += 1
            val = val << 1

        return res