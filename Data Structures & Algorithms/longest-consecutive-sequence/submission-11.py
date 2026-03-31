class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0

        for num in seq:
            if num - 1 not in seq:
                length = 0
                currVal = num
                while currVal in seq:
                    currVal += 1
                    length += 1
                longest = max(length, longest)

        return longest
