class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Step One: Flip Matrix Vertically
        matrix[:] = matrix[::-1]

        # Step Two: Transpose Matrix (Swap (x,y) to (y,x) positions)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i >= j:
                    continue

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
