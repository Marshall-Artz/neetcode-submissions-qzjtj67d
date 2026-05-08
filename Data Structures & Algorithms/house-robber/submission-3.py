class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem = {}
        def dfs(pos: int) -> int:
            if pos >= len(nums):
                return 0
            if pos in mem:
                return mem[pos]
            
            # Rob current house, or rob next house
            mem[pos] = max(
                nums[pos] + dfs(pos + 2),
                dfs(pos + 1)
            )
            return mem[pos]
        
        return dfs(0)

        # nums = [1,1,3,3]
        # pos  = 
        # cur  = 
        