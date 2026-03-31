class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        seq = set()
        mx  = 0
        
        for i, num in enumerate(nums):
            dic[num] = i
        
        print(dic)
        
        for num in nums:
            curr = num
            while curr-1 in dic.keys():
                print(curr)
                curr = curr - 1
            seq.add((curr, dic[curr]))

        for tup in seq:
            curr = tup[0]
            localMax = 0
            print("CURR:", curr)
            while curr in dic.keys():
                curr += 1
                localMax += 1
            mx = max(localMax, mx)
        
        return mx
