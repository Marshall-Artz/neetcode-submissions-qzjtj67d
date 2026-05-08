class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom Up:
        # trib = [0,1,1]

        # if n >= 0 and n < 3:
        #     return trib[n]

        # for i in range(3, n + 1):
        #     trib.append(
        #         trib[i - 3] + trib[i - 2] + trib[i - 1]
        #     )
        
        # return trib[-1]

        # Top Down:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        trib = [-1] * (n + 1)
        trib[0], trib[1], trib[2] = 0, 1, 1

        def dfs(i: int) -> int:
            # Base cases:
            if trib[i] != -1:
                return trib[i]

            trib[i] = dfs(i - 3) + dfs(i - 2) + dfs(i - 1)
            return trib[i]
        
        return dfs(n)