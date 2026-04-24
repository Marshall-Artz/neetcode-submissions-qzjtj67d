class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]
        digits.append(0)

        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        if digits[-1] == 0:
            digits.pop()
        
        return digits[::-1]