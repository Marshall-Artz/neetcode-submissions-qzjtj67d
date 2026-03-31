class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem = {}

        def dfs(pos: int, end: int) -> int:
            state = (pos, end)
            if state in mem:
                return mem[state]
            if pos >= end:
                return 0
            
            res = max(nums[pos] + dfs(pos + 2, end), dfs(pos + 1, end))
            mem[state] = res
            return res
        
        return max(
            dfs(0, len(nums) - 1),
            dfs(1, len(nums))
            )