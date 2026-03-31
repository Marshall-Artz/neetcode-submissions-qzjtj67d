class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums) - 1

        while bot <= top:
            mid = (top + bot) // 2
            print("bot:", nums[bot], " mid:", nums[mid], " top:", nums[top])

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bot = mid + 1
            elif nums[mid] > target:
                top = mid - 1

        return -1