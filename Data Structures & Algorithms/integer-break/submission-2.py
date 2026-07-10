class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        elif n == 3:
            return 2

        res = []

        while n:
            if n <= 3:
                res.append(n)
                n -= n
            else:
                res.append(3)
                n -= 3
        
        if res[-1] == 1:
            res[-2] -= 1
            res[-1] += 1
        
        return math.prod(res)

        # n   = 0
        # res = [3, 3, 3, 3]
        # return 81

        # n   = 0
        # res = [2, 2]
        # return 4