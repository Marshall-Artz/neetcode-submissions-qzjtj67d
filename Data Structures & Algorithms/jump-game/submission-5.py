class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        minIndex = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            dst = abs(minIndex - i)
            if nums[i] >= dst:
                minIndex = i
        
        return True if minIndex == 0 else False

        # nums       = [ 1,2,1,0,1]
        # minIndex   = 4
        # i, nums[i] = 0, 1
        # dst        = 4

        # nums       = [ 1,2,0,1,0]
        # minIndex   = 1
        # i, nums[i] = 0, 1
        # dst        = 0