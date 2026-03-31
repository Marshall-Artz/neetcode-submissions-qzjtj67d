class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxSum = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            maxSum = max(maxSum, curSum)
            curSum = max(curSum + nums[i], nums[i])
        
        return max(maxSum, curSum)