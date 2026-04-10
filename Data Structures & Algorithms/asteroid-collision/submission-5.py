class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids: # Loop through asteroids (left -> right)
            if stack and stack[-1] > 0 and ast <= 0:

                while (stack and # if stack not empty
                    stack[-1] > 0 and ast < 0 and # and top going right and ast going left
                    abs(stack[-1]) < abs(ast)): # and abs of top less than ast
                    stack.pop() # pop values off stack
                
                if stack and stack[-1] > 0 and ast < 0 and abs(stack[-1]) > abs(ast): # if top of stack is bigger:
                    continue # don't add ast
                
                if stack and stack[-1] > 0 and ast < 0 and abs(stack[-1]) == abs(ast): # if top of stack and ast are equal
                    stack.pop() # pop top of stack
                    continue # don't add ast
                
            stack.append(ast)
        
        return stack

        # stack = [-2, -2,]
        # asteroids = [-2, -2, 1, -2]

        # stack = [-2, -1, 1, 2]
        # asteroids = [-2, -1, 1, 2]
                
        # stack = [2]
        # asteroids = [2, 4, -4, -1]
        
        # stack = [5, 5]
        # asteroids = [5, 5]

        # stack = [7, 9]
        # asteroids = [7, -3, 9]


        # stack = [-4]
        # asteroids = [1, 1, 1, -4]

        # stack = [4]
        # asteroids = [4, -1, -1, -1]