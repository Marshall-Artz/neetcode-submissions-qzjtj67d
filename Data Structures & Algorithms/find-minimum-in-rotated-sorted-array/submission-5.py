class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot = 0
        top = len(nums) - 1
        z = 0
        while bot < top:
            mid = (bot + top) // 2
            print("bot:", nums[bot], " mid:", nums[mid], " top:", nums[top])
            if top - bot == 1:
                break
            elif nums[mid] < nums[top]:
                top = mid
            elif nums[mid] > nums[top]:
                bot = mid
            # z += 1
            # if z == 8: break
        
        return min(nums[bot], nums[top])