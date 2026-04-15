class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        count = 0

        for i in range(len(intervals) - 1):
            ls, le = intervals[i][0], intervals[i][1]
            rs, re = intervals[i + 1][0], intervals[i + 1][1]

            if rs < le:
                if le <= re: # Overwrite right interval to equal left
                    intervals[i + 1][0] = ls
                    intervals[i + 1][1] = le
                count += 1
        
        return count

    # intervals = [[1,2], [1,2], [2,3], [4,5]]
    # ls, le = 2, 3
    # rs, re = 4, 5
    # count  = 1
    
    # intervals = [[1,2], [2,4]]
    # ls, le = 1, 2
    # rs, re = 2, 4
    # count  = 0

    # intervals = [[1,2], [1,2], [2,4]]
    # ls, le = 1, 2
    # rs, re = 2, 4
    # count = 1

    # Greedy:
    # If they overlap, choose to delete
    # - Delete the intervals with the nearest end point
    # Else, continue