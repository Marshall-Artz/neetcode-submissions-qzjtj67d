class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def countSums(pos: int, val: int) -> int:
            if pos >= len(nums):
                return 1 if val == target else 0
            
            # Add or Subtract
            return countSums(pos + 1, val + nums[pos]) + countSums(pos + 1, val - nums[pos])
            
        
        return countSums(0, 0)