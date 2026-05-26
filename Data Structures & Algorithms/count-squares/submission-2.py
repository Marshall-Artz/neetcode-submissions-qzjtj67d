class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        i, j = point

        count = 0
        for (x, y), freq in self.points.items():
            # Exclude repeats of current point:
            if x == i and y == j:
                continue

            if (abs(x - i) == abs(y - j) and
                (x, j) in self.points and
                (i, y) in self.points):
                count += freq * self.points[(x, j)] * self.points[(i, y)]
            
        return count
                
    
    # this.points = [
    #     [1,1],
    #     [2,2],
    #     [1,2]
    # ]
    # point = [1,2]
    # comp  = [2,3]

    # this.points = [
    #     [1,1],
    #     [2,2],
    #     [1,2]
    # ]
    # comp  (x,y) = [1,2]
    # point (i,j) = [2,1]
