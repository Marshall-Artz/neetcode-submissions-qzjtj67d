class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = [0] * len(heights)

        for i, height in enumerate(heights):
            rec = height
            l = i - 1
            r = i + 1

            print("for height:", height)

            while l >= 0 and heights[l] >= height:
                print("heights[l]:", heights[l])
                l -= 1
            while r < len(heights) and heights[r] >= height:
                print("heights[r]:", heights[r])
                r += 1
            
            width = (r - l - 1)
            print("width:", width)
            rec = width * height
            
            res[i] = rec
        
        print(res)

        return max(res)