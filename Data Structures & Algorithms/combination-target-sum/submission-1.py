class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        s = []
        i = 0
        def dfs(i):
            if sum(s) == target:
                res.append(s.copy())
                return
            
            if i >= len(nums):
                return
            
            # Include number
            total = sum(s)
            s.append(nums[i])
            if nums[i] + total <= target:
                dfs(i)

            # Don't include number
            s.pop()
            dfs(i+1)
        
        dfs(i)
        return res