class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot = 0
        top = len(nums) - 1
        
        while bot < top:
            mid = (bot + top) // 2
            if nums[mid] < nums[top]:
                top = mid
            elif nums[mid] > nums[top]:
                bot = mid + 1
        
        return nums[bot]