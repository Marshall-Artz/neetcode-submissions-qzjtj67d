class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        mem = {}
        def countSums(pos: int, val: int) -> int:
            if (pos, val) in mem:
                return mem[(pos, val)]
            if pos >= len(nums):
                return 1 if val == target else 0
            
            # Add or Subtract
            mem[(pos, val)] = countSums(pos + 1, val + nums[pos]) + countSums(pos + 1, val - nums[pos])
            return mem[(pos, val)]
        
        return countSums(0, 0)