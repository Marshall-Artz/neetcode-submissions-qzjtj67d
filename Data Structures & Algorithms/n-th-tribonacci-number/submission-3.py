class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom Up:
        trib = [0,1,1]

        if n >= 0 and n < 3:
            return trib[n]

        for i in range(3, n + 1):
            trib.append(
                trib[i - 3] + trib[i - 2] + trib[i - 1]
            )
        
        return trib[-1]