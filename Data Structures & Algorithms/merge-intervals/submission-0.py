class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def overlaps(intA: List, intB: List):
            startA, endA = intA
            startB, endB = intB

            if (startA < startB and endA < startB or # All values left of intB
                startA > endB and endA > endB): # All values right of intB
                return False
            
            return True
        
        intervals.sort()
        stack = []

        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                startA, endA = interval
                startB, endB = stack[-1]

                if overlaps(interval, stack[-1]):
                    stack.pop()
                    newInterval = [min(startA, startB), max(endA, endB)]
                    stack.append(newInterval)
                else:
                    stack.append(interval)
        
        return stack

        # stack = [[1,2], [3,4], [5,6]]
        # intA  = [5, 6]
        # intB  = [3, 4]
        # intervals = [[1,2], [3,4], [5,6]]

        # stack = [[1, 5], [6, 7]]
        # intA  = [6, 7]
        # intB  = [1, 5]
        # intervals = [[1,3], [1,5], [6,7]]

        # stack = [[1,3]]
        # intA  = [2,3]
        # intB  = [1,2]
        # intervals = [[1,2], [2,3]]

        # stack = [[1, 3]]

        # stack = [[1, 5], [6,7]]

        # intervals = [[1,3], [1,5], [6, 7]]
        # intA = [1,3]
        # intB = [1,5]
        # s = [(1, 3), ]

        # intervals = [[1,2], [2,3]]
        # intA = [1,2]
        # intB = [2,3]
        # s = [(1,2), (1,3)]
