class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = [0] * len(heights)

        for i, height in enumerate(heights):
            rec = height
            l = i - 1
            r = i + 1

            while l >= 0 and heights[l] >= height:
                l -= 1
            while r < len(heights) and heights[r] >= height:
                r += 1
            
            width = (r - l - 1)
            rec = width * height
            
            res[i] = rec

        return max(res)