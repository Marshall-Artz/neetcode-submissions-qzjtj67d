class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val, count = nums[0], 0

        for num in nums:
            if val == num:
                count += 1
            elif count == 0:
                val = num
                count += 1
            elif val != num:
                count -= 1
            print(val, count)
        
        return val