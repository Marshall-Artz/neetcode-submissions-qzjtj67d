class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        newNums = []

        for num in nums:
            newNums.append(num)
        
        nums = sorted(newNums)

        if len(nums) == 1:
            return 1

        m = 1
        absMax = 0
        print(nums)

        for i, num in enumerate(nums):
            if i+1 < len(nums) and nums[i+1] == num + 1:
                m += 1
                absMax = max(m, absMax)
            else:
                m = 1
        
        return absMax
