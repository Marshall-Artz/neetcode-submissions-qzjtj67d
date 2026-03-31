class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        val = abs(x)
        neg = True if x < 0 else False

        length = len(str(val))

        for _ in range(10):
            if val == 0:
                break
            digit = val % 10
            res   = (res * 10) + digit
            val   = val // 10
        
        if res >= pow(2, 31):
            return 0
        
        return res if not neg else -res