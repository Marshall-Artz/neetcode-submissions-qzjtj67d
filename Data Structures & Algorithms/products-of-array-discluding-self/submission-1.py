class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res    = [1] * len(nums)
        preArr = [1] * len(nums)
        prePrd = 1
        posArr = [1] * len(nums)
        posPrd = 1

        for i, num in enumerate(nums):
            prePrd *= num
            preArr[i] = prePrd
        
        for i, num in enumerate(nums[::-1]):
            posPrd *= num
            posArr[i] = posPrd
        posArr = posArr[::-1]

        print("preArr:", preArr)
        print("posArr:", posArr)

        for i, num in enumerate(nums):
            if i-1 >= 0:
                leftProd = preArr[i-1]
            else:
                leftProd = 1
            if i+1 < len(nums):
                rightProd = posArr[i+1]
            else:
                rightProd = 1
            res[i] = leftProd * rightProd
            

        return res
