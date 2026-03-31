class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set()
        seq = set()
        mx  = 0
        
        for i, num in enumerate(nums):
            dic.add(num)
        
        for num in nums:
            curr = num
            while curr-1 in dic:
                curr = curr - 1
            seq.add(curr)

        for num in seq:
            curr = num
            localMax = 0
            while curr in dic:
                curr += 1
                localMax += 1
            mx = max(localMax, mx)
        
        return mx
