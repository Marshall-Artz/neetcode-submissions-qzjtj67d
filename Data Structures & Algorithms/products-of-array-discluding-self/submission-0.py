class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num

        if zeroCount > 1:
            return [0] * len(nums)
        elif zeroCount == 1:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            return res
        else:
            for num in nums:
                res.append(int(product / num))
            return res