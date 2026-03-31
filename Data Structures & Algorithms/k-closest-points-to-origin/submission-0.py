class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i, coord in enumerate(points):
            c = math.sqrt(pow(points[i][0], 2) + pow(points[i][1], 2))
            points[i] = [c, points[i][0], points[i][1]]
        
        heapq.heapify(points)
        print("min:", points[0])

        for i in range(k):
            cur = heapq.heappop(points)
            res.append([cur[1], cur[2]]) 
        
        print("points:", points)
        
        return res