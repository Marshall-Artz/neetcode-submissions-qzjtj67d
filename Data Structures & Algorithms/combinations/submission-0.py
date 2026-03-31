class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subarrs = []
        subarr  = []
        def dfs(i: int) -> None:
            if len(subarr) == k:
                subarrs.append(subarr.copy())
                return
            elif i > n:
                return
            
            # Include num at index i
            subarr.append(i)
            dfs(i + 1)
            subarr.pop()

            # Don't include num at index i
            dfs(i + 1)
        
        dfs(1)
        return subarrs