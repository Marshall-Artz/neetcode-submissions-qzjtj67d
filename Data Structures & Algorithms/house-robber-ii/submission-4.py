class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mem = {}

        def dfs(pos: int, end: int) -> int:

            if pos >= end:
                return 0
            if pos in mem:
                return mem[pos]
            
            mem[pos] = max(nums[pos] + dfs(pos + 2, end), dfs(pos + 1, end))

            return mem[pos]
        
        choice1 = dfs(0, len(nums) - 1)
        mem.clear()
        choice2 = dfs(1, len(nums))

        return max(choice1, choice2)