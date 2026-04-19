"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(len(intervals) - 1):
            end    = intervals[i].end
            nStart = intervals[i + 1].start

            if end > nStart:
                return False
        
        return True
    
    intervals = [(5,10), (0,4)]
    i     = 0
    end   = 10
    start = 0
    
    intervals = [(5,8), (9,15)]
    i      = 1
    end    = 8
    nStart = 9
    res = True

    intervals = [(0, 30), (5,10), (15,20)]
    i       = 0
    end     = 30
    nStart  = 5
    res = False