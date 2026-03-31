class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set()
        mxVal = 0

        for num in nums:
            dic.add(num)
        
        for num in nums:
            currVal = num
            while currVal in dic:
                currVal += 1
            if currVal - num > mxVal:
                mxVal = currVal - num
        
        return mxVal
