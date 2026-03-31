class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot = 0
        top = len(nums) - 1
        z = 0
        while top - bot > 1:
            mid = (bot + top) // 2
            print("bot:", nums[bot], " mid:", nums[mid], " top:", nums[top])
            if nums[mid] < nums[top]:
                top = mid
            elif nums[mid] > nums[top]:
                bot = mid
        
        return min(nums[bot], nums[top])