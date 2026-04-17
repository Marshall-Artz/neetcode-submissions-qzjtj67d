class Solution:
    def search(self, nums: List[int], target: int) -> int:

        bot, top = 0, len(nums) - 1

        while bot <= top:
            mid = (top + bot) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[mid] <= nums[top]: # Right side is sorted
                if target > nums[mid] and target <= nums[top]:
                    bot = mid + 1
                else:
                    top = mid - 1
            else: # Left side is sorted
                if target >= nums[bot] and target < nums[mid]:
                    top = mid - 1
                else:
                    bot = mid + 1
        
        return -1