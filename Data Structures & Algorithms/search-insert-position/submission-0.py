class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bot, top = 0, len(nums) - 1

        while bot <= top:
            mid = (bot + top) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                top = mid - 1
            elif nums[mid] < target:
                bot = mid + 1
        
        return top + 1