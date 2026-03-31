class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rev = heights[::-1]
        l = [-1] * len(heights)
        r = [-1] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                index = stack[-1][1]
                r[index] = i - index
                stack.pop()
            stack.append((heights[i], i))
        
        stack = []
    
        for i in range(len(rev)):
            while stack and stack[-1][0] > rev[i]:
                index = stack[-1][1]
                l[index] = i - index
                stack.pop()
            stack.append((rev[i], i))
        
        l = l[::-1]

        for i in range(len(l)):
            if l[i] == -1:
                l[i] = i+1

        r = r[::-1]

        for i in range(len(l)):
            if r[i] == -1:
                r[i] = i+1
        
        r = r[::-1]

        print(l)
        print(r)

        res = [0] * len(heights)
        for i, height in enumerate(heights):
            width = l[i] + r[i] - 1
            res[i] = width * height
        
        print(res)

        return max(res)