class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.i = 0
        res = []

        s = nums.copy()
        def dfs(i: int):
            if i >= len(nums):
                res.append(s.copy())
                return
            
            # Swap current i with all positions (self included):
            for j in range(i, len(nums)):
                # Swap i and j:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                dfs(i+1)
                
                # Swap i and j back
                s[j] = s[i]
                s[i] = temp
            
        
        dfs(self.i)
        return res