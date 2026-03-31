class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        NUMS = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        maxPast = nums[0]
        SUM = nums[0]
        for i in range(1, NUMS):
            if SUM + nums[i] >= nums[i]:
                SUM += nums[i]
                maxPast = max(maxPast, SUM)
            elif SUM + nums[i] < nums[i]:
                maxPast = max(maxPast, SUM)
                SUM = nums[i]
        
        return max(SUM, maxPast)