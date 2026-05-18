class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = set()
        rows = set()

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Loop through rows:
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        # Loop through cols:
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0
            

# matrix = [
#     [0,1],
#     [1,0]
# ]
# cols = {
#     0,
#     1
# }
# rows = {
#     0,
#     1
# }
