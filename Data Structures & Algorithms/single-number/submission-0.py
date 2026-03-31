class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)

        for key, value in d.items():
            if value == 1:
                return key