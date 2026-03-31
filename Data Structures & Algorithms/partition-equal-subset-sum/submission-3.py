class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        SUM = sum(nums)
        if SUM % 2 == 1:
            return False

        mem = {}

        def dfs(pos: int, target: int) -> bool:
            if (pos, target) in mem:
                return mem[(pos, target)]
            if pos >= len(nums) and target == 0:
                return True
            elif pos >= len(nums) and target != 0:
                return False

            # Include in first set or include in second set
            mem[(pos, target)] = dfs(pos + 1, target - nums[pos]) or dfs(pos + 1, target)

            return mem[(pos, target)]
        
        return dfs(0, SUM // 2)