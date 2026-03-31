class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums
        
        res = []
        
        n1, n2 = nums[0], nums[1]
        c1, c2 = 0, 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        c1, c2 = 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1

        res = []

        if n1 != None and c1 > (len(nums) / 3):
            res.append(n1)
        if n2 != None and c2 > (len(nums) / 3):
            res.append(n2)
        
        return res