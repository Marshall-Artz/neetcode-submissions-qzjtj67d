class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge = []
        res   = []
        start, end = newInterval

        for curStart, curEnd in intervals:
            if ((start < curStart and
                end < curStart) or
                (start > curEnd and
                end > curEnd)):
                res.append([curStart, curEnd])
            else:
                start = min(start, curStart)
                end   = max(end, curEnd)
        
        res.append([start, end])
        
        res.sort()

        return res