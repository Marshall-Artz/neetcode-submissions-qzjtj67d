class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        val = 1

        for i in range(32):
            if (n & val):
                res += 1
            val = val << 1

        return res