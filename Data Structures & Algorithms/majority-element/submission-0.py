class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = [0, 0]

        for key, val in counter.items():
            if val > res[1]:
                res[0], res[1] = key, val

        return res[0]