class Solution:
    def reverse(self, x: int) -> int:
        val = abs(x)
        res = 0

        for _ in range(10):
            if res > pow(2, 31):
                return 0
            if val == 0:
                break
            digit = val % 10
            res   = (res + digit) * 10
            val   = val // 10
        
        res = res // 10
        
        return res if x > 0 else -res