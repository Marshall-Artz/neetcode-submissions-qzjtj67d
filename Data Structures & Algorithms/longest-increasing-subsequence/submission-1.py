class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}

        def dfs(pos: int, last: int) -> int:
            if (pos, last) in mem:
                return mem[(pos, last)]
            if pos >= len(nums):
                return 0

            # First choice:
            # - Add to cur inc order
            choice1 = 0
            if nums[pos] > last:
                choice1 = 1 + dfs(pos + 1, nums[pos])

            # Second choice:
            # - Start new inc order
            choice2 = dfs(pos + 1, last)

            mem[(pos, last)] = max(choice1, choice2)
            return mem[(pos, last)]
        
        return dfs(0, float('-inf'))