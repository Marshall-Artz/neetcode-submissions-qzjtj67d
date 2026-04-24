class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = True
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
                break
        
        if carry == True:
            digits.insert(0, 1)
        
        return digits

        # digits == [1,0,0,0]
        # carry = True