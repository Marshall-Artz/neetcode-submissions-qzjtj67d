class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = set()
        mx  = 0
        
        for num in nums:
            if num - 1 not in nums:
                seq.add(num)

        for num in seq:
            curr = num
            localMax = 0
            while curr in nums:
                curr += 1
                localMax += 1
            mx = max(localMax, mx)
        
        return mx
