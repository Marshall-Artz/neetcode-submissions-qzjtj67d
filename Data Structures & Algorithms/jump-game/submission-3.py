class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        def dfs(pos: int) -> bool:
            if pos in mem:
                return mem[pos]
            if pos >= len(nums) - 1:
                return True
            
            for i in range(nums[pos], 0, -1):
                mem[pos] = dfs(i + pos)
                if mem[pos]: return True
            
            return False
        
        return dfs(0)