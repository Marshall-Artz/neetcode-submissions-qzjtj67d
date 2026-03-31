class Solution:
    def trap(self, heights: List[int]) -> int:
        totWater = 0
        reverseHeights = heights[::-1]
        l = [-1]
        lMax = -1
        r = [-1]
        rMax = -1

        for i in range(1, len(heights)):
            lMax = max(l[i-1], heights[i-1])
            l.append(lMax)
        
        print(l)

        for i in range(1, len(reverseHeights)):
            rMax = max(r[i-1], reverseHeights[i-1])
            r.append(rMax)
        
        r = r[::-1]

        print(r)

        for i in range(1, len(heights) - 1):
            waterCalc = min(l[i], r[i]) - heights[i]
            print(waterCalc)
            if waterCalc > 0:
                totWater += waterCalc
        
        return totWater