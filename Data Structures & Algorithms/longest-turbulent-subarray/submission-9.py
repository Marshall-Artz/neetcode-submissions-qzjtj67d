class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        mx  = 1
        res = [arr[0] - arr[1]]

        def dfs(pos: int, streak: int):
            nonlocal mx
            if pos >= len(arr):
                return
            
            prvSign = arr[pos - 2] - arr[pos - 1]
            curSign = arr[pos - 1] - arr[pos]
            
            # If fits, keep going with pattern:
            if ((prvSign < 0 and curSign > 0) or
                (prvSign > 0 and curSign < 0)):
                mx = max(mx, streak + 1)
                dfs(pos + 1, streak + 1)
            else:
                # Restart here:
                if curSign != 0:
                    mx = max(mx, 2)
                    dfs(pos + 1, 2)
                else:
                    dfs(pos + 1, 1)

        if arr[0] != arr[1]:
            mx = 2
            dfs(2, 2)
        else:
            dfs(1, 1)
        
        return mx