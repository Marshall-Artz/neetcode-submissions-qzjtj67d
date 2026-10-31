class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dic and dic[complement] != i:
                return [i, dic[complement]]
        
        return []

        # nums = [4,5,6], target = 10

        # dic  = {
        #     4: 0,
        #     5: 1,
        #     6: 2
        # }
        # i, num = 0, 4
        # complement = 10 - 4 = 6

        # return [0, 2]

        # nums = [/3,4,5,6], target = 7
        
        # dic  = {
        #     3: 0,
        #     4: 1,
        #     5: 2,
        #     6: 3
        # }
        # i, num = 0, 3
        # complement = 7 - 3 = 4

        # return [0, 1]

        