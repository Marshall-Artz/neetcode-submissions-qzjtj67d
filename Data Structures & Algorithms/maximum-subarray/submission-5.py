class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        mem = {}
        
        def dfs(pos: int, SUM: int) -> int:
            # Base cases
            if (pos, SUM) in mem:
                return mem[(pos, SUM)]
            if pos >= len(nums):
                return SUM

            # Include in sub arr or restart sub arr
            res1 = dfs(pos + 1, SUM + nums[pos])
            res2 = dfs(pos + 1, nums[pos])
            mem[(pos, SUM)] = max(SUM, res1, res2)

            return mem[(pos, SUM)]
        
        return dfs(1, nums[0])