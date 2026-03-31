class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums) - 1

        while bot <= top:
            middle = (bot + top) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                top = middle - 1
            elif nums[middle] < target:
                bot = middle + 1
        
        return -1


