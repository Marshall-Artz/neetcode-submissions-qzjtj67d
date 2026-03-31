class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        indexes = 0

        for i in range(1, len(nums) + 1):
            indexes = indexes ^ i

        xorNums = nums[0]
        for i in range(1, len(nums)):
            xorNums = xorNums ^ nums[i]
        
        return (xorNums ^ indexes)