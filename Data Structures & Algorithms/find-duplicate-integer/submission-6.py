class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        ptr  = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        
        while True:
            if nums[ptr] == nums[slow]:
                return nums[ptr]
            else:
                ptr = nums[ptr]
                slow = nums[slow]
                
            

        return -1