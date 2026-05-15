class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def valid(i: int, j: int) -> bool:
            if (i < 0 or i >= len(matrix) or
                j < 0 or j >= len(matrix[0])):
                return False
            
            return True

        i, j = 0, 0
        vis = set()

        vis.add((0,0))
        
        res = [matrix[0][0]]
        while len(res) < (len(matrix) * len(matrix[0])):
            # Top Row:
            while valid(i, j + 1) and (i, j + 1) not in vis:
                j += 1
                vis.add((i, j))
                res.append(matrix[i][j])

            # Right Row (Excluding Top Cell):
            while valid(i + 1, j) and (i + 1, j) not in vis:
                i += 1
                vis.add((i, j))
                res.append(matrix[i][j])

            # Bottom Row (Excluding Right Cell):
            while valid(i, j - 1) and (i, j - 1) not in vis:
                j -= 1
                vis.add((i, j))
                res.append(matrix[i][j])

            # Left Row (Excluding Bottom and Top Cell):
            while valid(i - 1, j) and (i - 1, j) not in vis:
                i -= 1
                vis.add((i, j))
                res.append(matrix[i][j])

        return res

        # matrix = [
        #     [1,2],
        #     [3,4]
        # ]

        # i, j = 1, 0
        # vis  = {
        #     (0,0),
        #     (0,1),
        #     (1,1),
        #     (1,0)
        # }
        # res  = [1,2,4,3]