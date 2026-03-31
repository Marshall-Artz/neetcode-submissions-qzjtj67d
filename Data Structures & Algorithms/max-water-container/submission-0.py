class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = -1

        for i, height in enumerate(heights):
            for j in range(i + 1, len(heights)):
                localMax = min(heights[i], heights[j]) * ((j + 1) - (i + 1))
                mx = max(localMax, mx)
        
        return mx