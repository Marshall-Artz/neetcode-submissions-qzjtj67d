class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval

        for i, (curStart, curEnd) in enumerate(intervals):
            if start < curStart and end < curStart:
                res.append([start, end])
                res += intervals[i:]
                break
            elif start > curEnd and end > curEnd:
                res.append([curStart, curEnd])
            else:
                start = min(start, curStart)
                end = max(end, curEnd)
        
        if not res or start > res[-1][0] and end > res[-1][1]:
            res.append([start, end])

        return res

        [[1, 5]]

        start, end = 6, 8
        curStart, curEnd = 1, 5