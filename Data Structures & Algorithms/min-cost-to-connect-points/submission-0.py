class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Pre-work, populate adjacency lists
        adj      = defaultdict(list)
        for x, y in points:
            for i, j in points:
                # Skip repeat match
                if x == i and y == j:
                    continue

                manDist = abs(x - i) + abs(y - j)
                adj[(x,y)].append((manDist,i,j))

        visit = set()
        front = [(0, points[0][0], points[0][1])] # Initialize with starting point
        cost  = 0

        while len(visit) != len(points):
            manDist, x, y = heapq.heappop(front)
            if (x,y) in visit:
                continue

            cost += manDist
            visit.add((x,y))

            for manDistChild, i, j in adj[(x,y)]:
                heapq.heappush(front, (manDistChild, i, j))
        
        return cost

        # points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
        # adj = {
        #     # (0,0): [(4,2,2), (6,3,3), (6,2,4), (6,4,2)],
        #     # (2,2): [(4,0,0), (2,3,3), (2,2,4), (2,4,2)],
        #     # (3,3): [(6,0,0), (2,2,2), (2,2,4), (2,4,2)],
        #     # (2,4): [(6,0,0), (2,2,2), (2,3,3), (4,4,2)],
        #     (4,2): [(6,0,0), (2,2,2), (2,3,3), (4,2,4)]
        # }
        # visit = {(0,0), (2,2), (2,4), (3,3), (4,2)}
        # front = [(2,4,2), (2,4,2), (4,0,0), (4,4,2), (6,0,0), (6,0,0), (6,2,4), (6,3,3), (6,4,2)]
        # cost  = 4 + 2 + 2 + 2
        # manDist, x, y = 2,4,2