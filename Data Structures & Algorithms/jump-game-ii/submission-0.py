class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        count = 0
        l = r = 0
        while r < len(nums) - 1:
            furthest = r
            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            l = r + 1
            r = furthest
            count += 1
        
        return count