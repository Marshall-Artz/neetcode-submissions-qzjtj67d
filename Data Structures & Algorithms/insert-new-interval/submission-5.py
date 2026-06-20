class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newL, newR = newInterval
        res = []

        for i, (intL, intR) in enumerate(intervals):
            
            # Interval comes before:
            if intR < newL:
                res.append([intL, intR])
            elif newR < intL: # newInterval comes before:
                res.append([newL, newR])
                res.extend(intervals[i:])
                return res
            else: # Interval Overlaps w/newInterval:
                newL, newR = min(intL, newL), max(intR, newR)
        
        res.append([newL, newR])
            
        return res