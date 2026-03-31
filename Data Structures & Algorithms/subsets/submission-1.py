class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        s = []
        i = 0
        def dfs(i):
            if i >= len(nums):
                res.append(s.copy())
                return
            
            # Include value at index
            s.append(nums[i])
            dfs(i + 1)
            
            # Don't include add value at index
            s.pop()
            dfs(i + 1)
        
        dfs(i)
        return res