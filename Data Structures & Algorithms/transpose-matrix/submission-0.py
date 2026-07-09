class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[-1 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        
        return res
        # [
        #     [ 2,1],
        #     [-1,3]
        # ]
        # len(matrix)    = 2
        # len(matrix[0]) = 2
        # [
        #     [-1,-1],
        #     [-1,-1]
        # ]
        
        # [
        #     [1,0,5],
        #     [2,4,3]
        # ]
        # len(matrix)    = 2
        # len(matrix[0]) = 3
        # [
        #     [1, 2],
        #     [0, 4],
        #     [5, 3]
        # ]