class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums) - 1
        z = 0
        while top - bot > 1:
            mid = (bot + top) // 2
            print("bot", nums[bot], " mid:", nums[mid], " top:", nums[top])
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[top] and nums[mid] < target and target < nums[top]: # Sorted top half
                bot = mid
            elif nums[mid] > nums[top] and (target < nums[top] or nums[mid] < target): # Unsorted top half
                bot = mid
            elif nums[bot] < nums[mid] and nums[bot] < target and target < nums[mid]: # Sorted bottom half
                top = mid
            elif nums[bot] > nums[mid] and (target < nums[mid] or nums[bot] < target): # Unsorted bottom half
                top = mid
            else:
                break
            z += 1
            if z == 8: break
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        if nums[bot] == target:
            return bot
        elif nums[top] == target:
            return top
        
        return -1
