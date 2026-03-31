class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pt1 = 0
        pt2 = len(heights) - 1
        maxWater = -1

        while pt1 < pt2:
            localWater = min(heights[pt1], heights[pt2]) * (pt2 - pt1)
            maxWater = max(localWater, maxWater)
            if heights[pt1] < heights[pt2]:
                pt1 += 1
            elif heights[pt1] > heights[pt2]:
                pt2 -= 1
            else:
                pt1 += 1 # TODO

        return maxWater