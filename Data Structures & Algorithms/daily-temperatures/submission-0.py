class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res   = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if i == 0 or len(stack) == 0:
                stack.append((temp, i))
                continue
            
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((temp, i))

        return res