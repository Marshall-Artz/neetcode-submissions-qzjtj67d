class Solution:
    def isHappy(self, n: int) -> bool:
        
        vis = set()
        while n:
            result = 0
            while n:
                digit = pow(n % 10, 2)
                n = n // 10
                result += digit
            
            n = result
            
            if result in vis:
                return False
            
            vis.add(result)

            if n == 1:
                return True

    # n = 2
    # vis = {
    #     2,

    # }
    # digit  = 1
    # result = 2
    
    # n = 1
    # vis = {
    #     1
    # }
    # digit  = 1
    # result = 1