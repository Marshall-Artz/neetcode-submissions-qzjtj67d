class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        ptr  = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(nums)
            print("slow:", nums[slow])
            print("fast:", nums[fast])
            if nums[slow] == nums[fast]:
                break
        
        print()
        print(nums)
        print("START slow:", nums[slow])
        print("ptr:", nums[ptr])
        while True:
            print(nums)
            print("slow:", nums[slow])
            print("ptr:", nums[ptr])
            if nums[ptr] == nums[slow]:
                return nums[ptr]
            else:
                ptr = nums[ptr]
                slow = nums[slow]
                
            

        return -1