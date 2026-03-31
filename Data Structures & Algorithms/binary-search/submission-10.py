class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums) - 1
        bot = 0

        while bot <= top:
            mid = (bot + top) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bot = mid + 1
            elif nums[mid] > target:
                top = mid - 1
        
        return -1


