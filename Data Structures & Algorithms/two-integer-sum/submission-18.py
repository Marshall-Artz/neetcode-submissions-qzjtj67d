class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            searchNum = (target - num)
            if searchNum in dic and dic[searchNum] != i:
                return [i, dic[searchNum]]
    
        return [-1, -1]

        # nums = [/3, 4, 5, 6], target = 7

        # dic = {
        #     3: 0,
        #     4: 1,
        #     5: 2,
        #     6: 3
        # }
        # searchNum = 7 - 3 = 4
        # return 0, 1