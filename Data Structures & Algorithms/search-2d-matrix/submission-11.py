class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottomRow = 0
        topRow    = len(matrix) - 1

        while bottomRow <= topRow:
            middleRow = (bottomRow + topRow) // 2
            if target in matrix[middleRow]:
                break
            elif target < matrix[middleRow][0]:
                topRow = middleRow - 1
            else:
                bottomRow = middleRow + 1

        row = matrix[middleRow]
        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            elif row[mid] > target:
                high = mid - 1

        return False