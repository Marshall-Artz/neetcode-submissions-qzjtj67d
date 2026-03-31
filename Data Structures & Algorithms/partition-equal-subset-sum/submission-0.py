class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        SUM = sum(nums)
        if SUM % 2 == 1:
            return False

        mem = {}

        def dfs(pos: int, sum1: int, sum2: int) -> bool:
            if (pos, sum1, sum2) in mem:
                return mem[(pos, sum1, sum2)]
            if pos >= len(nums) and sum1 == sum2:
                return True
            elif pos >= len(nums) and sum1 != sum2:
                return False

            # Include in first set or include in second set
            mem[(pos, sum1, sum2)] = dfs(pos + 1, sum1 + nums[pos], sum2) or dfs(pos + 1, sum1, sum2 + nums[pos])

            return mem[(pos, sum1, sum2)]
        
        return dfs(0, 0, 0)