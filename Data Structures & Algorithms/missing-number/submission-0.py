class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = set(nums)

        for i in range(len(nums) + 1):
            if i not in dic:
                return i