class Solution:
    def hammingWeight(self, n: int) -> int:
        res  = 0
        mask = 1

        for i in range(32):
            copy = mask & n
            if copy != 0:
                res += 1
            mask = mask << 1

        return res