class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildS = []
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == "*":
                wildS.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                elif wildS:
                    wildS.pop()
                else:
                    return False
        
        while stack and wildS:
            if stack[-1] < wildS[-1]:
                stack.pop()
                wildS.pop()
            else:
                break

        if not stack:
            return True

        return False