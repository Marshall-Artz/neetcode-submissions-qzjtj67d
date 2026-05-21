class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0

        if n > 0: # Positive n
            for i in range(n):
                res = res * x
        else:     # Negative n
            for i in range(abs(n)):
                res = res / x
        
        return res

        # x, n = 1.1, 10
        # res  = 2.357947691
        # i    = 7

        # x, n = 2.0, -3
        # res  = 0.125
        # i    = 3

        # x, n = 2.0, 5
        # res  = 32
        # i    = 5