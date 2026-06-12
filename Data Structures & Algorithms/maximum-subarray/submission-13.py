class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mem = {}
        def dfs(i: int, value: int) -> int:
            if (i, value) in mem:
                return mem[(i, value)]
            if i >= len(nums):
                return value
            
            # Keep going with current array or stop and start new array:
            mem[(i, value)] = max(
                value,
                dfs(i + 1, value + nums[i]),
                dfs(i + 1, nums[i])
            )

            return mem[(i, value)]
        
        return dfs(1,nums[0])