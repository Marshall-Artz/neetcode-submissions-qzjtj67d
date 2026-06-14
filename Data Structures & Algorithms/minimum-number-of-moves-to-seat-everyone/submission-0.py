class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        heapq.heapify(seats)
        heapq.heapify(students)

        res = 0

        for i in range(len(seats)):
            seat    = heapq.heappop(seats)
            student = heapq.heappop(students)

            res += abs(seat - student)
        
        return res

        # seats    = [1,2,4]
        # students = [1,3,3]
        # res      = 2
        # seat     = 4
        # student  = 3


        # seats    = [1,4,5,9]
        # students = [1,2,3,6]
        # res      = 7
        # seat     = 9
        # student  = 6