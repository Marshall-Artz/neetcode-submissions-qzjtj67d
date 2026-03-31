class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(pos: int) -> bool:
            if pos >= len(nums) - 1:
                return True
            
            print("AT:", nums[pos])
            
            for i in range(nums[pos], 0, -1):
                if dfs(i + pos): return True
            
            return False
        
        return dfs(0)