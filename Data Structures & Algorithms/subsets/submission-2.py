class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res    = []
        self.i = 0

        s   = []
        def dfs(i: int):
            if i >= len(nums):
                res.append(s.copy())
                return
            
            s.append(nums[i])
            dfs(i+1)

            s.pop()
            dfs(i+1)
        
        dfs(self.i)
        return res