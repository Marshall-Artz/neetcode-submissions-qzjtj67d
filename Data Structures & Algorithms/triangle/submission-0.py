class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        mem = {}
        def dfs(i: int, j: int) -> int:
            if (i, j) in mem:
                return mem[(i, j)]
            if i >= len(triangle):
                return 0
            
            # Move to i or i + 1
            mem[(i, j)] = min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
            return mem[(i, j)]
        
        return dfs(0,0)
        
        # triangle = [
        #     [2],
        #    [3,4],
        #   [6,5,7],
        #  [4,1,8,3]
        # ]

        # dfs(0,0)
        #     3 + 5 + 1 + 0