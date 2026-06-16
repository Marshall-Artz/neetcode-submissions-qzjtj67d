class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx     = float('-inf')
        curMax = 0

        for num in nums:
            curMax += num
            mx = max(mx, curMax)

            if curMax < 0:
                curMax = 0
        
        return mx
        
        # nums   = [-1]
        # mx     = -1
        # curMax = 0

        # nums   = [2,-3,4,-2,2,1,-1, 4]
        # mx     = 8
        # curMax = 8