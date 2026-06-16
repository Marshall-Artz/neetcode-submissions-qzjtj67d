class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = float('-inf')
        curSum   = 0

        for num in nums:
            curSum += num
            totalSum = max(totalSum, curSum)
            if curSum < 0:
                curSum = 0
        
        totalMin = float('inf')
        curMin   = 0

        for num in nums:
            curMin += num
            totalMin = min(totalMin, curMin)
            if curMin > 0:
                curMin = 0
        
        if sum(nums) == totalMin:
            return totalSum

        return max(
            sum(nums) - totalMin,
            totalSum
        )

        # nums       = [-2,4,-5,4,-5,9, 4]
        # totalSum   = 13
        # curSum     = 13
        # totalMin   = -6
        # curMin     = 0

        # return 15
        
        # nums     = [2,3, -4]
        # totalSum = 5
        # curSum   = 1