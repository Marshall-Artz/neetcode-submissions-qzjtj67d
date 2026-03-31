class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(pos: int) -> int:
            # Base case:
            if pos in mem:
                return mem[pos]
            if pos >= len(nums):
                return 0

            mem[pos] = max(nums[pos] + dfs(pos + 2), nums[pos] + dfs(pos + 3))

            return mem[pos]
        
        return max(dfs(0), dfs(1))