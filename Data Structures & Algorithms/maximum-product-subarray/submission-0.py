class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        globalMax = nums[0]
        
        prevMin = prevMax = prevArr = nums[0]
        for i in range(1, len(nums)):
            curArr = nums[i]
            curMin = min(prevMin * nums[i], prevMax * nums[i], nums[i])
            curMax = max(prevMin * nums[i], prevMax * nums[i], nums[i])

            prevArr = curArr
            prevMin = curMin
            prevMax = curMax

            globalMax = max(globalMax, curMin, curMax)
        
        return globalMax