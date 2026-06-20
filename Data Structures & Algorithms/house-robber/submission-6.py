class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = {}
        def dfs(i: int) -> int:
            if i in mem:
                return mem[i]
            if i >= len(nums):
                return 0
            
            # Rob house or don't rob house:
            mem[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return mem[i]
        
        return dfs(0)