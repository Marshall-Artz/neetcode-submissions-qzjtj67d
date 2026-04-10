class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val, count = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == val:
                count += 1
            elif nums[i] != val:
                if count == 1:
                    val = nums[i]
                    continue
                else:
                    count -= 1
        
        return val